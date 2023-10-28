''' commands that work with redis '''
from json import dumps, loads

import requests

from api.huntwordsapi.models.puzzle import Puzzle


def command_puzzle_load(**kwargs):
    url = kwargs['--url']
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

        data = f'{{ "oper": "puzzle-updated", "body": {jpuzzle} }}'
        print(f'calling {url} with:')
        print(data)
        r = requests.post(url, data)

        print(f'status_code={r.status_code}')
        print(f'reason={r.reason}')
        print(f'text={r.text}')


def command_puzzles(**kwargs):
    url = kwargs['--url']

    r = requests.post(url, '{ "oper": "puzzles", "body": {} }')

    print(f'status_code={r.status_code}')
    print(f'reason={r.reason}')
    print(f'text={r.text}')
