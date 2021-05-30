from pymongo import MongoClient
import json

class database:

    def __init__(self):
        self._client = MongoClient("mongodb+srv://bekirsencan:Turtoise@cluster0.vfdtl.mongodb.net/YksApp?retryWrites=true&w=majority")
        self._db = self._client.get_database('YksApp')
        self._profile_collection = self._db.get_collection('Profile')
        self._university_collection = self._db.get_collection('Target_university')
        self._lessons_collection = self._db.get_collection('Lessons')
        self._tyt_university_collection = self._db.get_collection('Tyt_university')
        self._workout_collection = self._db.get_collection('Workout')





