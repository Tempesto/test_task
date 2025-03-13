import requests

from api.logger import Logger
from config import BASE_URL, TOKEN


class APISession:
    BASE_URL = BASE_URL

    def __init__(self):
        self._token = TOKEN

    def get(self, relative_path: str, **kwargs):
        Logger.add_request(method='GET', url=relative_path, **kwargs)
        response = self.make_request('GET', relative_path, **kwargs)
        Logger.add_response(response)

        return response

    def post(self, relative_path: str, **kwargs):
        Logger.add_request(method='POST', url=relative_path, json=kwargs)
        response = self.make_request('POST', relative_path, **kwargs)
        Logger.add_response(response)

        return response

    def put(self, relative_path: str, **kwargs):
        Logger.add_request(method='PUT', url=relative_path, **kwargs)
        response = self.make_request('PUT', relative_path, **kwargs)
        Logger.add_response(response)

        return response

    def patch(self, relative_path: str, **kwargs):
        Logger.add_request(method='PATCH', url=relative_path, **kwargs)
        response = self.make_request('PATCH', relative_path, **kwargs)
        Logger.add_response(response)

        return response

    def delete(self, relative_path: str, **kwargs):
        Logger.add_request(method='DELETE', url=relative_path, **kwargs)
        response = self.make_request('DELETE', relative_path, **kwargs)
        Logger.add_response(response)

        return response

    def make_request(self, method: str, relative_path: str, **kwargs):
        url = self._build_request_url(relative_path)
        headers = self.get_default_headers()
        headers.update(kwargs.pop('headers', {}))
        Logger.add_headers_and_accept_language(headers=headers)

        return requests.request(method=method, url=url, headers=headers, **kwargs)

    def _build_request_url(self, relative_path: str):
        return f'{self.BASE_URL}{relative_path}'

    def get_default_headers(self):
        headers = {'content-type': 'application/json'}
        if self._token:
            headers['Authorization'] = f'Bearer {self._token}'

        return headers
