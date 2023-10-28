'''eliminate circular references by placing these shared definitions in their own module'''

from dataclasses import dataclass
from typing import Any


@dataclass
class Request:
    oper: str
    body: dict

    def __iter__(self):
        yield 'oper', self.oper
        yield 'body', self.body


def request_from_dict(d: dict) -> Request:
    return Request(
        d['oper'],
        d['body']
    )


@dataclass
class Response:
    statusCode: int
    body: Any
    headers: dict

    def __iter__(self):
        yield 'statusCode', self.statusCode
        yield 'body', self.body
        yield 'headers', self.headers
