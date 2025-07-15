from fastapi import FastAPI, HTTPException

from .models.endpoint import Endpoint, EndpointResponse

admin_app = FastAPI(title="端点管理 API", description="用于管理和维护所有可用端点，包括端点的增删查等操作。适合平台管理员使用，保障端点配置的统一和安全。")  # noqa: RUF001


@admin_app.get("/endpoints", response_model=list[EndpointResponse], summary="列出所有端点", description="获取所有已注册端点的详细信息")
def list_endpoints():
    """
    列出所有端点
    """
    from .store import db

    return [{"name": name, **dict(db[name])} for name in db]


@admin_app.post("/endpoints/{name}", summary="添加端点", description="添加一个新的端点")
def add_endpoint(name: str, endpoint: Endpoint) -> EndpointResponse:
    """添加端点"""
    from .store import db

    if name in db:
        raise HTTPException(400, "Endpoint already exists")
    db[name] = endpoint
    return {"name": name, **endpoint.model_dump()}  # type: ignore


@admin_app.delete("/endpoints/{name}", summary="删除端点", description="根据名称删除指定端点")
def delete_endpoint(name: str):
    """删除端点"""
    from .store import db

    if name not in db:
        raise HTTPException(404, "Endpoint not found")
    del db[name]

    return {"ok": True}
