import json
from datetime import datetime

from .model.puzzle import get_puzzle
from .model.puzzleboard import PuzzleBoard, push_puzzleboard


class HuntwordsPuzzleBoardComsumedCommand(object):
    '''Command class that processes puzzleboard-consumed message'''

    def run(self, jreq):
        '''Command that procsses puzzleboard-consumed message'''

        resp = json.loads(jreq)

        puzzle = get_puzzle(resp['puzzleboard'])
        size = int(resp['size'])

        pboard = PuzzleBoard(size, size, [], [], puzzle)
        jpboard = json.dumps(dict(pboard))

        push_puzzleboard(puzzle.name, jpboard)

        resp["processed"] = {
            "at": f"{datetime.now().isoformat()}",
            "status": "ok"
        }

        return json.dumps(resp)
