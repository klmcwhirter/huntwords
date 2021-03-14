import redis


def redis_client():
    r = redis.Redis(host='redis.redis', port=6379, db=0)
    return r
