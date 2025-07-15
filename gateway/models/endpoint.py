from pydantic import BaseModel, Field, HttpUrl


class Endpoint(BaseModel):
    """端点配置"""

    base_url: HttpUrl = Field(description="你原本的 OpenAI-compatible API 的 base url", examples=["https://api.example.com/v1"])
    api_key: str = Field(description="我们请求你的 API 时的 Bearer Token", examples=["sk-..."])


class EndpointResponse(Endpoint):
    """端点返回信息"""

    name: str = Field(description="端点名称")
