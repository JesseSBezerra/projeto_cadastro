from pymongo import MongoClient
import uuid

client = MongoClient('localhost', 27017, userName='cadastro', password='cadastro')
db = client['cadastro']
collection = db['cadastro']


def save(object):
    object['_id'] = str(uuid.uuid4())
    collection.insert_one(object)
    return object


def update(object):
    collection.update_one({'_id': object['_id']}, {'$set': object})
    return object


def delete(id):
    collection.delete_one({'_id': id})
    return id


def find_by_name(name):
    data = collection.find_one({'nome': name})
    return data
