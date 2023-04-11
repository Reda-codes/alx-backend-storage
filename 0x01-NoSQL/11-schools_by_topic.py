#!/usr/bin/env python3
""" schools_by_topic: Python function that returns the list of school having a specific topic """


def schools_by_topic(mongo_collection, topic):
    ''' schools_by_topic function'''
    cursor = mongo_collection.find({"topics": {"$in": [topic]}})
    return list(cursor)
