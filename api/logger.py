import json
import os
import traceback
from datetime import datetime

from requests import Response


class Logger:
    date_now = str(datetime.now().strftime('%Y-%m-%d_%H:%M'))
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    log_dir = os.path.join(project_root, 'logs')
    filename = os.path.join(log_dir, 'log_' + date_now + '.log')
    logs = []

    @classmethod
    def _write_log_to_file(cls, data: str):
        with open(cls.filename, 'a', encoding='utf-8') as logger_file:
            logger_file.write(data)
        cls.logs.append(data)

    @classmethod
    def add_request(cls, url: str = None, method: str = None, json: dict = None, **kwargs):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')
        foo = traceback.extract_stack()

        data_to_add = '\n-----\n'
        data_to_add += f'Test: {test_name}\n'
        data_to_add += f'Name function: {foo[-3][2]}\n'
        data_to_add += f'Data: {datetime.now()}\n'
        data_to_add += f'Request method: {method}\n'
        data_to_add += f'Request URL: {url}\n'
        data_to_add += f'Request data: {json}\n'

        cls._write_log_to_file(data_to_add)

    @classmethod
    def add_headers_and_accept_language(cls, headers: dict):
        data_to_add = f'Request headers: {headers}\n'
        data_to_add += '\n'

        cls._write_log_to_file(data_to_add)

    @classmethod
    def add_response(cls, response: Response):
        headers_as_dict = dict(response.headers)
        try:
            response_json = response.json()
            response_text = json.dumps(response_json, indent=4, ensure_ascii=False)
        except ValueError:
            response_text = response.text

        data_to_add = f'Date {datetime.now()}\n'
        data_to_add += f'Response code: {response.status_code}\n'
        data_to_add += f'Response headers: {headers_as_dict}\n'
        data_to_add += f'Response text: {response.text}\n'

        data_to_add += '\n-----\n'

        cls._write_log_to_file(data_to_add)

        cls.last_response = {'text': response_text}
