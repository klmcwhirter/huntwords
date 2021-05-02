'''eliminate circular references by placing these shared definitions in their own module'''

from dataclasses import dataclass

@dataclass
class Event:
    body: str
    headers: str
    method: str
    query: str
    path: str


@dataclass
class Response:
    statusCode: int
    body: str
    headers: dict
