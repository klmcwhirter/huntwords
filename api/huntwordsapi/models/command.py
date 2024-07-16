'''eliminate circular references by placing these shared definitions in their own module'''

from dataclasses import dataclass
from typing import Any


@dataclass
class CommandRequest:
    oper: str
    body: dict

    def __iter__(self):
        yield 'oper', self.oper
        yield 'body', self.body


def request_from_dict(d: dict) -> CommandRequest:
    if 'oper' not in d or 'body' not in d:
        return CommandRequest('invalid oper', {})

    return CommandRequest(
        d['oper'],
        d['body']
    )


@dataclass
class CommandResponse:
    statusCode: int
    body: Any
    headers: dict

    def __iter__(self):
        yield 'statusCode', self.statusCode
        yield 'body', self.body
        yield 'headers', self.headers
