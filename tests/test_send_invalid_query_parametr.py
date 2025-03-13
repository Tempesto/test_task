import pytest

from api.constants.error_message import ErrorMessage
from api.constants.http_status_codes import HttpStatusCodes
from api.services.chat_completions import send_message


@pytest.mark.xfail(reason='Server should return 400 status code, but returns 500')
@pytest.mark.invalid_parameters
def test_send_request_with_invalid_parameters(api_session):
    data = {
        'stream': True,
        'temperature': 0.4,
        'top_p': 1,
        'n': 1,
        'presence_penalty': 0,
        'frequency_penalty': 0,
        'model': 'gpt-4-0125-preview',
        'messages': [],
    }
    response = send_message(
        session=api_session,
        data=data,
        status_code=HttpStatusCodes.BAD_REQUEST,
    )
    assert response['message'] == ErrorMessage.REQUEST_FAILED
