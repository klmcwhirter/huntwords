''' commands for the manager cli '''

from uuid import uuid4

from .post_api_request import post_api_request


def command_puzzleboards_clear(**kwargs):
    url = kwargs['--url']
    body = f'{{ "oper": "puzzleboards-clear", "body": {{"correlation-id": "{uuid4()}"}} }}'

    post_api_request('command_puzzleboards_clear', url, body)


def command_puzzleboard_consume(**kwargs):
    url = kwargs['--async-url']
    name = kwargs['--name']
    size = kwargs['--size']
    body = f'{{ "oper": "puzzleboard-consumed", "body": {{"puzzle": "{name}", "size": {size}, "correlation-id": "{uuid4()}"}} }}'

    post_api_request('command_puzzleboard_consume', url, body)


def command_puzzleboard_count(**kwargs):
    url = kwargs['--url']
    name = kwargs['--name']
    body = f'{{ "oper": "puzzleboard-count", "body": {{"puzzle": "{name}", "correlation-id": "{uuid4()}"}} }}'

    post_api_request('command_puzzleboard_count', url, body)


def command_puzzleboard_pop(**kwargs):
    url = kwargs['--url']
    name = kwargs['--name']
    body = f'{{ "oper": "puzzleboard-pop", "body": {{"puzzle": "{name}", "correlation-id": "{uuid4()}"}} }}'

    post_api_request('command_puzzleboard_pop', url, body)
