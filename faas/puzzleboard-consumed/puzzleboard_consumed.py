import json
from datetime import datetime
from random import choice

import redis


class HuntwordsPuzzleBoardComsumedCommand(object):
    '''Command class that processes puzzleboard-consumed message'''

    def run(self, jreq):
        '''Command that procsses puzzleboard-consumed message'''

        resp = json.loads(jreq)

        val = self.tickle_redis()

        status = choice(['pending', 'ok', 'error'])
        resp["processed"] = {
            "at": f"{datetime.now().isoformat()}",
            "foo": val,
            "status": status
        }

        return json.dumps(resp)

    def tickle_redis(self):
        r = redis.Redis(host='redis.redis', port=6379, db=0)
        r.set('foo', 'bar')
        val = r.get('foo')
        return val.decode('utf-8')
