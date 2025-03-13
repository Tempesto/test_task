from api.constants.http_status_codes import HttpStatusCodes
from api.constants.urls.chat import CHAT_COMPLETIONS
from api.helpers.assert_status_code import assert_status_code
from api.models.chat_completion_request import ChatCompletionRequest
from dataclasses import asdict


def send_message(
    session,
    data: ChatCompletionRequest | dict,
    status_code=HttpStatusCodes.SUCCESS.value,
):
    """Send message to chat completions."""
    if isinstance(data, ChatCompletionRequest):
        data = asdict(data)
    if data.get('stream'):
        response = session.post(CHAT_COMPLETIONS, json=data, stream=True)
        assert_status_code(response, status_code)
        if response.status_code != HttpStatusCodes.SUCCESS:
            return response.json()
        return response.iter_lines()

    else:
        data = asdict(data)
        response = session.post(CHAT_COMPLETIONS, json=data)
        assert_status_code(response, status_code)
        response_data = response.json()
        if response.status_code != HttpStatusCodes.SUCCESS.value:
            return response

        return response_data
