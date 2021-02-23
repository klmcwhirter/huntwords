''' commands for the manager cli '''

from uuid import uuid4

import requests


def command_consume(**kwargs):
    url = kwargs['--url']
    r = requests.post(url, f'{{"puzzleboard": "fruit", "correlation-id": "{uuid4()}"}}')

    print(f'status_code={r.status_code}')
    print(f'reason={r.reason}')
    print(f'text={r.text}')
