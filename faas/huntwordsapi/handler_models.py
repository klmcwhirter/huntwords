'''eliminate circular references by placing these shared definitions in their own module'''

from dataclasses import dataclass

@dataclass
class Event:
    body: str
    headers: str
    method: str
    query: str
    path: str

    def __iter__(self):
        yield 'body', self.body
        yield 'headers', self.headers
        yield 'method', self.method
        yield 'query', self.query
        yield 'path', self.path


@dataclass
class Response:
    statusCode: int
    body: str
    headers: dict

    def __iter__(self):
        yield 'statusCode', self.statusCode
        yield 'body', self.body
        yield 'headers', self.headers
