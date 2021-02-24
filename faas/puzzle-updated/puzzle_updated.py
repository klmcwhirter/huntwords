import json

import redis

from model.puzzle import puzzle_urn, Puzzle


class HuntwordsPuzzleUpdatedCommand(object):
    '''Command class that processes puzzle-updated message'''

    def run(self, jreq):
        '''Command that processes puzzle-updated message'''

        obj = json.loads(jreq)
        puzzle = Puzzle(obj['name'], obj['description'], obj['words'])
        dpuzzle = dict(puzzle)

        self.set_puzzle(puzzle['name'], dpuzzle)

        return json.dumps({'status': 'ok', 'puzzle': dict(puzzle)})

    def set_puzzle(self, name, puzzle):
        r = redis.Redis(host='redis.redis', port=6379, db=0)
        r.set(puzzle_urn(name), puzzle)
