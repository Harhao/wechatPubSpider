__author__ = 'Administrator'
import pymongo
class MongoOperate(object):
    def __init__(self,mongo_uri,mongo_db,mongo_user,mongo_pass,collection):
        self.mongo_uri=mongo_uri
        self.mongo_db=mongo_db
        self.mongo_user=mongo_user
        self.mongo_pass=mongo_pass
        self.collection=collection
    def connect(self):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        self.db.authenticate(self.mongo_user,self.mongo_pass)
    def finddata(self):
        return self.db[self.collection].find({})