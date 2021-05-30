from database import database
from flask import Response
import json


class tyt_university(database):

    def __init__(self):
        super().__init__()
    
    def search_university(self,query):
        print(query)
        cursor = self._tyt_university_collection.aggregate(
            [{
            '$match':query
        },{
            "$project":{"_id":0}
        }])
        result = []
        for data in cursor:
            result.append(data)
        return Response(json.dumps(result),mimetype='application/json')