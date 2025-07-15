from fastapi import Depends, FastAPI
from fastapi.responses import StreamingResponse

from .admin import admin_app
from .models.chat import ChatRequest, ChatResponse
from .utils.client import new_client

app = FastAPI(
    title="Moderation Gateway",
    description=("提供多合一的针对对话补全接口的审核网关，支持流式和非流式响应。适用于聚合多种大模型服务，便于统一接入和权限管理。"),  # noqa: RUF001
)
app.mount("/admin", admin_app)


def get_endpoint(endpoint: str):
    from .store import get_endpoint_by_name

    return get_endpoint_by_name(endpoint)


@app.post("/{endpoint}/chat/completions", response_model=ChatResponse, summary="对话补全", description="根据输入消息生成对话补全结果，支持流式和非流式返回")  # noqa: RUF001
async def chat_completions(
    data: ChatRequest,
    endpoint=Depends(get_endpoint),
):
    """对话补全接口"""
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
