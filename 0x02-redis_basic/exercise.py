#!/usr/bin/env python3
'''
exercise file
'''
import redis
import uuid


class Cache:
    '''
    class Cache that handless memory cache
    '''
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: [str, int, float, bytes]) -> str:
        '''
        method that takes a data argument and returns a string
        '''
        uid = str(uuid.uuid4())
        try:
            self._redis.set(uid, data)
            return uid
        except redis.RedisError as e:
            return(f"Error: {e}")
