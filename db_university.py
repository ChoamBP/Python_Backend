from flask import Response
from encoder import JSONEncoder
from database import database
from university import university
from bson.objectid import ObjectId

unv = university.get_instance()

class target_university(database):

   __instance__ = None

   @staticmethod
   def get_instance():
      if not target_university.__instance__:
         target_university()
      return target_university.__instance__
    
   def __init__(self):
      super().__init__()
      if target_university.__instance__ is None:
         target_university.__instance__ = self
      else:
         raise Exception("You cannot create another class")
    
   def add_new_target(self):
      self._university_collection.insert(
         {
            "_id":ObjectId(unv.object_id),
            "section":unv.section,
            "target_university":unv.target_university,
            "target_department":unv.target_department,
            "target_point":unv.target_point
         }
      )
      return "true"

   def delete_current_target(self,obj_id):
      self._university_collection.delete_one(
         {
         "_id":ObjectId(obj_id)
         }
      )
      return "true"
   
   def update_target(self):
      self._university_collection.update_one(
         {
            "_id":ObjectId(unv.object_id)
         },
         {
            '$set':{
            "section":unv.section,
            "target_university":unv.target_university,
            "target_department":unv.target_department,
            "target_point":unv.target_point
            }
         }
      )
      return "true"
   
   def get_current_university_data(self,object_id):
      json_data = self._university_collection.find_one(
         {
            "_id":ObjectId(object_id)
         }
      )
      return Response(JSONEncoder().encode(json_data),mimetype='application/json')
      