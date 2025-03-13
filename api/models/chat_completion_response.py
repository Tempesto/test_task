from dataclasses import dataclass
from typing import List, Any, Optional


@dataclass
class MessageContent:
    """Dataclass for message content."""

    role: str
    content: str
    refusal: Optional[Any] = None


@dataclass
class Choice:
    """Dataclass for choice."""

    index: int
    message: MessageContent
    finish_reason: str
    logprobs: Optional[Any] = None


@dataclass
class TokensDetails:
    """Dataclass for tokens details."""

    cached_tokens: int = 0
    audio_tokens: int = 0
    reasoning_tokens: int = 0
    accepted_prediction_tokens: int = 0
    rejected_prediction_tokens: int = 0


@dataclass
class UsageInfo:
    """Information about usage tokens."""

    prompt_tokens: int
    completion_tokens: int
    total_tokens: int
    prompt_tokens_details: TokensDetails
    completion_tokens_details: TokensDetails


@dataclass
class ChatCompletionResponse:
    """Dataclass for chat completion response."""

    id: str
    object: str
    created: int
    model: str
    choices: List[Choice]
    usage: UsageInfo
    service_tier: str
    system_fingerprint: str
