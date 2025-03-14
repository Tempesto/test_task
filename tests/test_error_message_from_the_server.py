import pytest

from api.constants.error_message import ErrorMessage
from api.constants.http_status_codes import HttpStatusCodes
from api.services.chat_completions import send_message


@pytest.mark.error_message_from_the_server
def test_server_return_500_status_code_and_error_message(api_session):
    data = {
        'stream': True,
        'temperature': 0.4,
        'top_p': 1,
        'n': 1,
        'presence_penalty': 0,
        'frequency_penalty': 0,
        'model': 'gpt-4-0125-preview',
        'messages': [
            {
                'role': 'user',
            }
        ],
    }
    response = send_message(
        session=api_session,
        data=data,
        status_code=HttpStatusCodes.INTERNAL_SERVER_ERROR,
    )
    assert response['message'] == ErrorMessage.REQUEST_FAILED
