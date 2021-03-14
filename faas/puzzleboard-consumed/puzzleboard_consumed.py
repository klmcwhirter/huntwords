import json
from datetime import datetime
from random import choice

import redis


class HuntwordsPuzzleBoardComsumedCommand(object):
    '''Command class that processes puzzleboard-consumed message'''

    def run(self, jreq):
        '''Command that procsses puzzleboard-consumed message'''

        resp = json.loads(jreq)

        val = self.tickle_redis(resp['puzzleboard'])

        status = choice(['pending', 'ok', 'error'])
        resp["processed"] = {
            "at": f"{datetime.now().isoformat()}",
            "puzzle": val,
            "status": status
        }

        return json.dumps(resp)

    def tickle_redis(self, name):
        r = redis.Redis(host='redis.redis', port=6379, db=0)
        r.set('puzzle', name)
        val = r.get('puzzle')
        return val.decode('utf-8')
