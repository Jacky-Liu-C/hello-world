# 将MongoDB的find, insert, update, remove方法封装成类

from pymongo import MongoClient

class MongodbClient(object):

    def __init__(self):
        self.client = MongoClient(
            host='127.0.0.1',
            port=27017
        )
        self.db = self.client['company']
        self.col = self.db['workers']

    def find(self):
        cur = self.col.find()
        return cur

    def insert_one(self, dict):
        res = self.col.insert_one(dict)
        return res

    def insert_many(self, dict_list):
        res = self.col.insert_many(dict_list)
        return res

    def update_one(self, filter, update):
        res = self.col.update_one(filter, update)
        return res

    def update_many(self, filter, update):
        res = self.col.update_many(filter, update)
        return res

    def delete_one(self, filter):
        res = self.col.delete_one(filter)
        return res

    def delete_many(self, filter):
        res = self.col.delete_many(filter)
        return res

dict_data = [
    {'name':'jacky', 'age':28, 'sex':'M' },
    {'name':'tom', 'age':34, 'sex':'F' },
    {'name':'puny', 'age':55, 'sex':'M' },
    {'name':'kunbi', 'age':18, 'sex':'F' }
]

if __name__ == '__main__':
    mongo = MongodbClient()
    # mongo.insert_many(dict_data)
    # mongo.insert_one({'name':'sdfsfdsafd', 'age':111, 'sex':'AASD' })
    # mongo.delete_one({'age':111})
    # mongo.delete_many({'name':'tom'})

    # myquery = {"name": 'kunbi'}    #  'kunbi' 可替换成正侧 {"$regex": "^F"}
    # newvalues = {"$set": {"name": "lucy"}}  # $set
    # x = mongo.update_many(myquery, newvalues)
    # print(x.modified_count, "个文档已修改")

    x = mongo.update_one({'age':18},{'$set':{'sex':'M'}})
    print(x.modified_count, x.raw_result, x.matched_count, sep='\n')
    # 更新数，更新结果，匹配数
    print(mongo.find())
    for doc in mongo.find():
        print(doc)










