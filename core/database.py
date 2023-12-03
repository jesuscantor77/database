from pymongo import MongoClient

def link(db = ''):
    client = MongoClient('mongodb://localhost:27017/')
    db = client[db]
    return db