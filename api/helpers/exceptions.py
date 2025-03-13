from requests import Response


class APIException(BaseException):
    """Base class for all API exceptions."""


class UnexpectedResponseStatus(APIException):
    def __init__(self, response: Response):
        self._response = response

    def __str__(self) -> str:
        return (
            f'Request to {self._response.url} failed. Server responded with '
            f'unexpected status {self._response.status_code}: '
            f'{self._response.content}'
        )

    @property
    def response(self) -> Response:
        return self._response
