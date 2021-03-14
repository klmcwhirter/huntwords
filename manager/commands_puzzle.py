''' commands that work with redis '''
from json import dumps, loads

import requests

from faas.model.puzzle import Puzzle


def command_puzzle_load(**kwargs):
    url = kwargs['--load-url']
    filename = kwargs['--file']

    jpuzzle = '{}'
    with open(filename, 'r') as f:
        jpuzzle = f.read()
    obj = loads(jpuzzle)

    for p in obj:
        # This part of the code serves to validate the json structure from the file just read.
        puzzle = Puzzle(p['name'], p['description'], p['words'])
        dpuzzle = dict(puzzle)
        jpuzzle = dumps(dpuzzle)

        print(f'calling {url} with:')
        print(jpuzzle)
        r = requests.post(url, jpuzzle)

        print(f'status_code={r.status_code}')
        print(f'reason={r.reason}')
        print(f'text={r.text}')
