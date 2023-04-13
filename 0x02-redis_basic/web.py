#!/usr/bin/env python3
''' web.py file '''
import requests
import redis
import uuid


def get_page(url: str) -> str:
    ''' get_page function '''
    client = redis.Redis()
    cached = client.get(url)
    if cached:
        return cached
    else:
        client.incr(f"count:{url}")
        response = requests.get(url).content.decode('utf-8')
        client.setex(url, 10, response)
        return response
