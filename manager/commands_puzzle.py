''' commands that work with redis '''
from json import dumps, loads

from api.huntwordsapi.models.puzzle import Puzzle

from .post_api_request import post_api_request


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

        body = f'{{ "oper": "puzzle-updated", "body": {jpuzzle} }}'

        post_api_request('command_puzzle_load', url, body)


def command_puzzles(**kwargs):
    url = kwargs['--url']
    body = '{ "oper": "puzzles", "body": {} }'
    post_api_request('command_puzzles', url, body)
