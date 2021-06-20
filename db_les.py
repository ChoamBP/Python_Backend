from database import database
from user import user
from bson.objectid import ObjectId
from encoder import JSONEncoder
from flask import Response
from flask.json import jsonify
import json
import success_rate as rate


class lessons(database):

    __instance__ = None
    

    @staticmethod
    def get_instance():
        if not lessons.__instance__:
            lessons()
        return lessons.__instance__
    

    def __init__(self):
        super().__init__()
        if lessons.__instance__ is None:
            lessons.__instance__ = self
        else:
            raise Exception("You cannot create another class")
    
    def get_json_from_database(self,object_id):
        json_data = self._lessons_collection.find_one(
            {
                "_id":ObjectId(object_id)
            }
        )
        return json_data
    
    def update_by_arg(self,update_name,lesson_type,object_id,data):
        switcher = {
            'matematik':lambda:self.update_lesson(object_id,update_name,lesson_type,data),
            'geometri':lambda:self.update_lesson(object_id,update_name,lesson_type,data),
            'edebiyat':lambda:self.update_lesson(object_id,update_name,lesson_type,data),
            'turkce':lambda:self.update_lesson(object_id,update_name,lesson_type,data),
            'fizik':lambda:self.update_lesson(object_id,update_name,lesson_type,data),
            'kimya':lambda:self.update_lesson(object_id,update_name,lesson_type,data),
            'biyoloji':lambda:self.update_lesson(object_id,update_name,lesson_type,data),
            'tarih':lambda:self.update_lesson(object_id,update_name,lesson_type,data),
            'cografya':lambda:self.update_lesson(object_id,update_name,lesson_type,data),
            'felsefe & din kültürü':lambda:self.update_lesson(object_id,update_name,lesson_type,data)
        }
        return switcher.get(update_name,lambda:'Invalid')()
    
    def update_lesson(self,object_id,lesson_name,lesson_type,data):
        self._lessons_collection.update_one({
            "_id":ObjectId(object_id)
        },{
            "$set":{f"{lesson_type}.{lesson_name}":data}
        })
        return "true"
    
    def get_lesson(self,object_id,lesson_type,lesson_name):
        json_data = self._lessons_collection.find_one(
            {
                "_id":ObjectId(object_id)
            },
            {
                "_id":0,
                f"{lesson_type}.{lesson_name}":1
            }
        )
        return Response(JSONEncoder().encode(json_data.get(lesson_type).get(lesson_name)),mimetype='application/json')
    
    def set_new_user(self,data):
        self._lessons_collection.insert_one(data)
