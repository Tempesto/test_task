import pytest

from api.helpers.streaming_validation import validate_chunks
from api.models.chat_completion_request import ChatCompletionRequest
from api.services.chat_completions import send_message


@pytest.mark.chat_completions_stream_true
def test_send_request_to_the_chat_with_corect_token_and_parameters(api_session):
    data = ChatCompletionRequest()
    response = send_message(session=api_session, data=data)
    validate_chunks(response)
