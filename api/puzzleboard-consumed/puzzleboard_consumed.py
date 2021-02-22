from datetime import datetime
import json


class HuntwordsPuzzleBoardComsumedCommand(object):
    '''Command class that processes puzzleboard-consumed message'''

    def run(self, jreq):
        '''Command that procsses puzzleboard-consumed message'''

        resp = json.loads(jreq)

        resp['processed'] = {'at': datetime.now()}

        return resp
