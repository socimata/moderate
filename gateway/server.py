from fastapi import Depends, FastAPI
from fastapi.responses import StreamingResponse

from .admin import admin_app
from .models.chat import ChatRequest, ChatResponse
from .utils.client import new_client

app = FastAPI()
app.mount("/admin", admin_app)


def get_endpoint(endpoint: str):
    from .store import get_endpoint_by_name

    return get_endpoint_by_name(endpoint)


@app.post("/{endpoint}/chat/completions", response_model=ChatResponse)
async def chat_completions(
    data: ChatRequest,
    endpoint=Depends(get_endpoint),
):
    if data.stream:

        async def stream():
            async with new_client(endpoint) as client, client.stream("POST", "/chat/completions", json=data.model_dump(exclude_unset=True)) as response:
                async for chunk in response.aiter_bytes():
                    yield chunk

        return StreamingResponse(stream(), media_type="text/event-stream")

    else:
        async with new_client(endpoint) as client:
            res = await client.post("/chat/completions", json=data.model_dump(exclude_unset=True))
            res.raise_for_status()
            return res.json()
