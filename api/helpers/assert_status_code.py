from api.exceptions import UnexpectedResponseStatus


def assert_status_code(data, code):
    if data.status_code != code:
        raise UnexpectedResponseStatus(data)
