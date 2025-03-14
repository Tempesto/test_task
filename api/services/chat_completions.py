from api.constants.http_status_codes import HttpStatusCodes
from api.constants.urls.chat import CHAT_COMPLETIONS
from api.helpers.assert_status_code import assert_status_code
from api.models.chat_completion_request import ChatCompletionRequest
from dataclasses import asdict


def send_message(
    session,
    data: ChatCompletionRequest | dict,
    status_code=HttpStatusCodes.SUCCESS,
):
    """Send message to chat completions."""
    if isinstance(data, ChatCompletionRequest):
        data = asdict(data)

    is_stream = bool(data.get('stream'))
    response = session.post(CHAT_COMPLETIONS, json=data, stream=is_stream)
    assert_status_code(response, status_code)

    if response.status_code != HttpStatusCodes.SUCCESS.value:
        return response.json() if is_stream else response

    return response.iter_lines() if is_stream else response.json()
