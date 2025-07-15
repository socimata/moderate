from fastapi import FastAPI, HTTPException

from .models.endpoint import Endpoint, EndpointResponse

admin_app = FastAPI()


@admin_app.get("/endpoints", response_model=list[EndpointResponse])
def list_endpoints():
    from .store import db

    return [{"name": name, **dict(db[name])} for name in db]


@admin_app.post("/endpoints/{name}")
def add_endpoint(name: str, endpoint: Endpoint) -> EndpointResponse:
    from .store import db

    if name in db:
        raise HTTPException(400, "Endpoint already exists")
    db[name] = endpoint
    return {"name": name, **endpoint}


@admin_app.delete("/endpoints/{name}")
def delete_endpoint(name: str):
    from .store import db

    if name not in db:
        raise HTTPException(404, "Endpoint not found")
    del db[name]

    return {"ok": True}
