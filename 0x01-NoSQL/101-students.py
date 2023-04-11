#!/usr/bin/env python3
""" top_students: Python function that returns all students sorted by average score: """


def top_students(mongo_collection):
    ''' top_students function'''
    return mongo_collection.aggregate([{"$project": {"name": 1, "averageScore": {"$avg": "$topics.score"}}}, {"$sort": {"averageScore": -1}}])
