from typing import TypedDict

from pydantic import HttpUrl


class Endpoint(TypedDict):
    base_url: HttpUrl
    api_key: str


class EndpointResponse(Endpoint):
    name: str
