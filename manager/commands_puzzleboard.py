''' commands for the manager cli '''

from uuid import uuid4

import requests


def command_puzzleboard_consume(**kwargs):
    url = kwargs['--consume-url']
    name = kwargs['--name']
    r = requests.post(url, f'{{"puzzleboard": "{name}", "correlation-id": "{uuid4()}"}}')

    print(f'status_code={r.status_code}')
    print(f'reason={r.reason}')
    print(f'text={r.text}')
