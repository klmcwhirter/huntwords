import json
from datetime import datetime
from random import choice

import redis


class HuntwordsPuzzleUpdatedCommand(object):
    '''Command class that processes puzzle-updated message'''

    def run(self, jreq):
        '''Command that processes puzzle-updated message'''

        resp = json.loads(jreq)

        val = self.tickle_redis()

        status = choice(['pending', 'ok', 'error'])
        resp["processed"] = {
            "at": f"{datetime.now().isoformat()}",
            "bar": val,
            "status": status
        }

        return json.dumps(resp)

    def tickle_redis(self):
        r = redis.Redis(host='redis.redis', port=6379, db=0)
        r.set('bar', 'foo')
        val = r.get('bar')
        return val.decode('utf-8')
