import pytest

from api.api_session import APISession
from api.constants.error_message import ErrorMessage
from api.constants.http_status_codes import HttpStatusCodes
from api.models.chat_completion_request import ChatCompletionRequest
from api.services.chat_completions import send_message


@pytest.mark.invalid_token
def test_send_request_with_invalid_token():
    api_session = APISession()
    api_session._token = 'invalid_token'
    data = ChatCompletionRequest()
    response = send_message(
        session=api_session,
        data=data,
        status_code=HttpStatusCodes.UNAUTHORIZED,
    )
    assert response['message'] == ErrorMessage.UNAUTHORIZED
