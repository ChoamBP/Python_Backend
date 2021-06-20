from bson.objectid import ObjectId
from flask import Response
from database import database


class success_rate(database):

    def __init__(self):
        super().__init__()

    
    def new_user_rate(self,object_id,username):
        self._success_rate_collection.insert(
            {
                "_id":ObjectId(object_id),
                "username":username,
                "score":0
            }
        )
    
    def set_user_rate(self,object_id,score):
        self._success_rate_collection.update_one(
            {
                "_id":ObjectId(object_id)
            },
            {
                "$set":{"score":score}
            }
        )
        return "true"
    
    def get_all_user_rate(self):
        cursor = self._success_rate_collection.aggregate([
            {},{"_id":0}
        ])
        result = []
        for data in cursor:
            result.append(data)
        new_list = sorted(result,key=lambda k: k['score'])
        new_list.reverse()
        return Response(new_list,mimetype='application/json')
