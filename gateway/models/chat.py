from typing import Literal

from promplate import Context
from pydantic import BaseModel


class ChatRequest(BaseModel):
    model: str
    messages: list[Context]
    temperature: float | None = None
    stream: bool = False


class Choice(BaseModel):
    index: Literal[0]
    message: Context
    finish_reason: str


class ChatResponse(BaseModel):
    id: str
    model: str
    object: Literal["chat.completion"]
    choices: tuple[Choice]
    created: int
