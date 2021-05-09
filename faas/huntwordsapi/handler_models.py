'''eliminate circular references by placing these shared definitions in their own module'''

from dataclasses import dataclass


@dataclass
class Request:
    oper: str
    body: str

    def __iter__(self):
        yield 'oper', self.oper
        yield 'body', self.body


def request_from_dict(d: dict) -> Request:
    return Request(
        d['oper'],
        d['body']
    )


@dataclass
class Event:
    body: str
    headers: str
    method: str
    query: str
    path: str
    request: Request

    def __iter__(self):
        yield 'body', self.body
        yield 'headers', self.headers
        yield 'method', self.method
        yield 'query', self.query
        yield 'path', self.path
        yield 'request', dict(self.request)


@dataclass
class Response:
    statusCode: int
    body: str
    headers: dict

    def __iter__(self):
        yield 'statusCode', self.statusCode
        yield 'body', self.body
        yield 'headers', self.headers
