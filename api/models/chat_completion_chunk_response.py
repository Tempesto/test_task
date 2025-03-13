from dataclasses import dataclass
from typing import List, Optional, Any


@dataclass
class DeltaContent:
    """Dataclass for delta content in streaming chunk."""

    content: Optional[str] = None


@dataclass
class StreamingChoice:
    """Dataclass for choice in streaming chunk."""

    index: int
    delta: DeltaContent
    finish_reason: Optional[str] = None


@dataclass
class ChatCompletionChunkResponse:
    """Dataclass for chat completion chunk response (streaming)."""

    id: str
    object: str
    created: int
    model: str
    choices: List[StreamingChoice]
    service_tier: Optional[str] = None
    usage: Optional[Any] = None
    system_fingerprint: Optional[str] = None
