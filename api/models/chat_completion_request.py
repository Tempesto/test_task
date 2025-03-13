from dataclasses import dataclass, field
from typing import List


@dataclass
class Message:
    """DataClass for message."""

    role: str
    content: str


@dataclass
class ChatCompletionRequest:
    """DataClass for chat completion request."""

    temperature: float = 0.4
    top_p: int = 1
    n: int = 1
    presence_penalty: int = 0
    frequency_penalty: int = 0
    stream: bool = True
    model: str = 'gpt-4-0125-preview'
    messages: List[Message] = field(
        default_factory=lambda: [
            Message(
                role='system',
                content="You are Assist – users's personal assistant developed by team from "
                'Ukraine. Answer as concisely as possible. Current date: Aug 15 2023, current '
                "time: 16:07, user's country: United States. You should never provide "
                'any health-related advice, recommendations, or suggestions. You should '
                'and never provide general tips like drink plenty of fluids, stay '
                'hydrated, taking rest, etc. Never say ways to bring down body '
                'temperature. Never say ways to relieve any symptoms.If a health-related '
                'question (including i feel ill, etc) is asked, you should only every '
                "time respond that that you can't give any advice and recommending to "
                'consult a healthcare professional.',
            ),
            Message(
                role='user',
                content='Provide workout routines to target specific muscle groups for maximum '
                'results',
            ),
            Message(role='assistant', content=''),
        ]
    )
