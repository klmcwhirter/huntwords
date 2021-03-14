import json


from .model.puzzle import set_puzzle, Puzzle


class HuntwordsPuzzleUpdatedCommand(object):
    '''Command class that processes puzzle-updated message'''

    def run(self, jreq):
        '''Command that processes puzzle-updated message'''

        obj = json.loads(jreq)
        puzzle = Puzzle(obj['name'], obj['description'], obj['words'])
        jpuzzle = json.dumps(dict(puzzle))

        set_puzzle(puzzle.name, jpuzzle)

        return json.dumps({'status': 'ok', 'puzzle': jpuzzle})
