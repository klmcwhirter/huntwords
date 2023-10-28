import os
import redis


def redis_client():
    host = os.environ['REDIS_HOST'] if 'REDIS_HOST' in os.environ else 'redis'
    port_str = os.environ['REDIS_PORT'] if 'REDIS_PORT' in os.environ else '6379'
    port = int(port_str)

    r = redis.Redis(host=host, port=port, db=0)
    return r
