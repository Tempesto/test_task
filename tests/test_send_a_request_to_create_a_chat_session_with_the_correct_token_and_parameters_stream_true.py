import pytest

from api.models.chat_completion_request import ChatCompletionRequest
from api.models.chat_completion_response import ChatCompletionResponse
from api.services.chat_completions import send_message

@pytest.mark.chat_completions_stream_false
def test_send_request_to_the_chat_with_corect_token_and_parameters(api_session):
    data = ChatCompletionRequest(stream=False)
    response = send_message(session=api_session, data=data)
    try:
        ChatCompletionResponse(**response)
    except TypeError as e:
        raise AssertionError(f'Error in response: {e}')

