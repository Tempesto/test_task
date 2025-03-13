from api.constants.http_status_codes import HttpStatusCodes
from api.constants.urls.chat import CHAT_COMPLETIONS
from api.helpers.assert_status_code import assert_status_code


def send_message(
    session,
    data,
    status_code=HttpStatusCodes.CREATED.value,
):
    """Send message to chat completions."""
    response = session.post(CHAT_COMPLETIONS, json=data)
    assert_status_code(response, status_code)
    response_data = response.json()
    if response.status_code != HttpStatusCodes.CREATED.value:
        return response_data

    return response_data
