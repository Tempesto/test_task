from enum import StrEnum


class ErrorMessage(StrEnum):
    UNAUTHORIZED = 'Unauthorized'
    REQUEST_FAILED = 'Request failed with status code 400'
