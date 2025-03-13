import dataclasses
import json

from api.constants.http_status_codes import HttpStatusCodes
from api.constants.urls.chat import CHAT_COMPLETIONS
from api.helpers.assert_status_code import assert_status_code
from api.models.chat_completion_request import ChatCompletionRequest
from dataclasses import asdict


def send_message(
    session,
    data: ChatCompletionRequest,
    status_code=HttpStatusCodes.SUCCESS.value,
):
    """Send message to chat completions."""
    if data.stream:
        data = asdict(data)
        full_response_content = ""

        with session.post(CHAT_COMPLETIONS, json=data, stream=True) as response:
            assert_status_code(response, status_code)
            for line in response.iter_lines():
                if line:
                    try:
                        chunk = json.loads(line)
                        if 'choices' in chunk and chunk['choices']:
                            delta_content = chunk['choices'][0]['delta'].get('content')
                            finish_reason = chunk['choices'][0].get('finish_reason')

                            if delta_content:
                                full_response_content += delta_content

                            if finish_reason == "stop":
                                break

                    except json.JSONDecodeError:
                        print(f"Error decoding JSON: {line.decode('utf-8')}")

        return full_response_content

    else:
        data = asdict(data)
        response = session.post(CHAT_COMPLETIONS, json=data)
        assert_status_code(response, status_code)
        response_data = response.json()
        if response.status_code != HttpStatusCodes.SUCCESS.value:
            return  response

        return response_data
