import json

import pytest
from pytest_check import check

from api.constants.streaming import DONE_MARKER, SSE_DATA_PREFIX
from api.models.chat_completion_chunk_response import ChatCompletionChunkResponse


def validate_chunks(response_iterator):
    """Validate basic fields in streaming chunks for a positive scenario."""
    chunk_count = 0

    for line in response_iterator:
        if line:
            chunk_count += 1
            decoded_line = line.decode('utf-8')

            if decoded_line == DONE_MARKER:
                break

            if not decoded_line.startswith(SSE_DATA_PREFIX):
                pytest.fail(f'Not correct format streaming chunk: {decoded_line}')

            json_payload = decoded_line[len(SSE_DATA_PREFIX) :]
            if not json_payload.strip():
                continue

            try:
                chunk_json = json.loads(json_payload)
                chunk_response_obj = ChatCompletionChunkResponse(**chunk_json)
                with check:
                    assert chunk_response_obj.id, (
                        f"Chunk #{chunk_count}: Line 'id' empty or" f' missing'
                    )
                with check:
                    assert chunk_response_obj.object == 'chat.completion.chunk', (
                        f"Chunk #{chunk_count}: Line 'object' mast be 'chat.completion.chunk', "
                        f"get '{chunk_response_obj.object}'"
                    )
                with check:
                    assert isinstance(chunk_response_obj.choices, list), (
                        f"Chunk #{chunk_count}: Line 'choices' mast be list, "
                        f"get '{type(chunk_response_obj.choices)}'"
                    )
                for idx, choice in enumerate(chunk_response_obj.choices):
                    with check:
                        assert (
                            'delta' in choice
                        ), f"Chunk #{chunk_count}, choice #{idx}: 'delta' відсутній"

            except json.JSONDecodeError as e:
                raise AssertionError(f'Chunk #{chunk_count}: JSON decode error: {e}') from e
            except TypeError as e:
                raise AssertionError(
                    f'Chunk #{chunk_count}: JSON not parsed to ChatCompletionChunkResponse: {e}'
                ) from e

    return chunk_count
