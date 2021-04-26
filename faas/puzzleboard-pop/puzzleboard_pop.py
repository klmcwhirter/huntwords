import json
from datetime import datetime

import requests

from .model.puzzleboard import pop_puzzleboard


class HuntwordsPuzzleBoardPopCommand(object):
    '''Command class that processes puzzleboard-pop message'''

    def run(self, jreq):
        '''Command that processes puzzleboard-pop message'''

        req = json.loads(jreq)

        pboard = pop_puzzleboard(req['puzzle'])
        jpboard = json.dumps(dict(pboard))

        resp = {
            'puzzleboard': jpboard,
            'processed': {
                'at': f'{datetime.now().isoformat()}',
                'status': 'ok'
            }
        }

        send_consumed(pboard)

        return json.dumps(resp)


def send_consumed(pboard):
    '''Send async request to generate a new copy'''
    url = '/async-function/puzzleboard-consumed'
    data = f'{{"puzzle": "{pboard.puzzle.name}" }}'

    requests.post(url, data)
