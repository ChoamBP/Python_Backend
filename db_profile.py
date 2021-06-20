from database import database
from user import user
from db_university import target_university
from bson.objectid import ObjectId
from encoder import JSONEncoder
from flask import Response

from lesson_class import json_lessons
from success_rate import success_rate


usr = user.get_instance()

class profile(database):

   __instance__ = None

   @staticmethod
   def get_instance():
      if not profile.__instance__:
         profile()
      return profile.__instance__
    
   def __init__(self):
      super().__init__()
      if profile.__instance__ is None:
         profile.__instance__ = self
      else:
         raise Exception("You cannot create another class")


   def add_new_user(self):
      self._profile_collection.insert(
            {
            "username":usr.username,
            "password":usr.password,
            "name":usr.name,
            "email":usr.email,
            "profile_picture_url":usr.profile_picture_url,
            "gender":usr.gender,
            "class":usr.user_class
            }
        )
      new_object_id = self.get_user_object_id(usr.username)
      cls_lesson = json_lessons()
      cls_lesson.new_user(new_object_id)
      rate = success_rate()
      rate.new_user_rate(new_object_id,usr.username)
      return "true"
   
   def get_user_object_id(self,username):
      data = self._profile_collection.find_one({
         "username":username
      },{
         "_id":1
      })
      return data["_id"]
   
   def delete_user_by_id(self,object_id):
      self._profile_collection.delete_one(
         {
            "_id":ObjectId(object_id)
         }
      )
      return "true"
   
   def update_user(self):
      self._profile_collection.update_one(
         {
            "_id":ObjectId(usr.object_id)
         },
         {
            '$set':{
            "username":usr.username,
            "password":usr.password,
            "name":usr.name,
            "email":usr.email,
            "profile_picture_url":usr.profile_picture_url,
            "class":usr.user_class
            }
         }
      )
      return "true"
   
   def check_existing(self,username,password):
      data = self._profile_collection.find_one(
         {
            '$and':[
               { 'username':username },
               { 'password':password }
            ]
         },
         { '_id':1 }
      )
      return self.get_user_data(data['_id'])
   
   def get_all_users_data(self):
      all_data = self._profile_collection.find()
      result = []
      for data in all_data:
         result.append(data)
      return Response(JSONEncoder().encode(result),mimetype='application/json')
   
   def get_user_data(self,object_id):
      json_data = self._profile_collection.find_one(
         {
            "_id":ObjectId(object_id)
         }
      )
      return Response(JSONEncoder().encode(json_data),mimetype='application/json')

   def check_username(self,username):
      try:
         self._profile_collection.find_one(
            {
               "username":username
            }
         )
         return "true"
      except:
         return "false"