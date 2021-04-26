''' commands for the manager cli '''

from uuid import uuid4

import requests


def command_puzzleboard_consume(**kwargs):
    url = kwargs['--consume-url']
    name = kwargs['--name']
    size = kwargs['--size']
    data = f'{{"puzzle": "{name}", "size": {size}, "correlation-id": "{uuid4()}"}}'
    print(data)

    r = requests.post(url, data)

    print(f'status_code={r.status_code}')
    print(f'reason={r.reason}')
    print(f'text={r.text}')


def command_puzzleboard_pop(**kwargs):
    url = kwargs['--pop-url']
    name = kwargs['--name']
    data = f'{{"puzzle": "{name}", "correlation-id": "{uuid4()}"}}'
    print(data)

    r = requests.post(url, data)

    print(f'status_code={r.status_code}')
    print(f'reason={r.reason}')
    print(f'text={r.text}')
