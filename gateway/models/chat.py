from typing import Literal

from promplate import Message
from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """对话请求体"""

    model: str = Field(description="模型名称")
    messages: list[Message] = Field(description="消息列表")
    temperature: float | None = Field(None, description="采样温度")
    stream: bool = Field(False, description="是否以流式返回")


class Choice(BaseModel):
    """对话响应选项"""

    index: Literal[0] = Field(description="选项索引")
    message: Message = Field(description="消息内容")
    finish_reason: str = Field(description="结束原因")


class ChatResponse(BaseModel):
    """对话响应体"""

    id: str = Field(description="响应 ID")
    model: str = Field(description="模型名称")
    object: Literal["chat.completion"] = Field(description="对象类型")
    choices: tuple[Choice] = Field(description="选项列表")
    created: int = Field(description="创建时间戳")
