from database import database
from bson.objectid import ObjectId
import datetime
from flask import Response
import json

class workout(database):

    def __init__(self):
        super().__init__()

    def set_new_workout(self,json_data):
        self._workout_collection.insert_one({
            "username":json_data.get("username"),
            "lesson_name":json_data.get("lesson_name"),
            "subject":json_data.get("subject"),
            "info":json_data.get("info"),
            "start_time":json_data.get("start_time"),
            "end_time":json_data.get("end_time"),
            "date":json_data.get("date"),
        })
        return "true"
    
    def get_workouts(self,username):
        cursor = self._workout_collection.aggregate([
            {
                '$match':{"username":username}
            },{
                "$project":{"_id":0}
            }
        ])
        result = []
        for data in cursor:
            result.append(data)
        print(result)
        return Response(json.dumps(result),mimetype='application/json')

