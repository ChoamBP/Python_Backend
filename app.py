from flask import Flask,request,Response
from flask_restful import Api 
import con_profile as con_profile
import con_university as con_university
from flask_cors import CORS
import db_les as les
import lesson_class as lesson_class
import university_query_generator
import workout as work_class
import success_rate as rate



app = Flask(__name__)
CORS(app)

#user get-post
@app.route('/api/user/register',methods=['POST'])
def api_register_user():
    json_data = request.get_json()
    return con_profile.set_new_profile_model(json_data)

@app.route('/api/user/delete/<string:objectid>',methods=['GET'])
def api_delete_user(objectid):
    return con_profile.delete_user(objectid)

@app.route('/api/user/update',methods=['POST'])
def api_update_user():
    json_data = request.get_json()
    return con_profile.set_profile_model(json_data)

@app.route('/api/user/get_all_users',methods=['GET'])
def get_all_users_data():
    return con_profile.get_all_users()

@app.route('/api/user/check_username/<string:username>',methods=['GET'])
def get_cur_user(username):
    return con_profile.get_user_profile(username)

@app.route('/api/user/check_user/<string:username>/<string:password>',methods=['GET'])
def check_user(username,password):
    return con_profile.user_exist_check(username,password)

#university get-post
@app.route('/api/university/new_target',methods=['POST'])
def new_target_uni():
    json_data = request.get_json()
    return con_university.set_new_target_university(json_data)

@app.route('/api/university/delete_target/<string:objectid>',methods=['GET'])
def delete_target_uni(objectid):
    return con_university.delete_current_target(objectid)

@app.route('/api/university/update_target',methods=['POST'])
def update_target_uni():
    json_data = request.get_json()
    return con_university.set_university_model(json_data)

@app.route('/api/university/get_data/<string:objectid>',methods=['GET'])
def get_university_data(objectid):
    return con_university.get_current_target(objectid)



# get and post lesson
@app.route('/api/lessons/get_data/<string:object_id>', methods=['GET'])
def get_data(object_id):
    a = lesson_class.json_lessons()
    return a.send_response(object_id)

@app.route('/api/lessons/update_one_lesson',methods=['POST'])
def update_lesson():
    json_data = request.get_json()
    a = les.lessons.get_instance()
    obj_id = json_data.get("_id")
    lesson_name = json_data.get("lesson_name")
    lesson_type = json_data.get("type")
    subject_state = json_data.get("subject_state")
    return a.update_by_arg(lesson_name,lesson_type,obj_id,subject_state)

@app.route('/api/lessons/get_one_lesson/<string:object_id>/<string:lesson_type>/<string:lesson_name>',methods=['GET'])
def get_lesson(object_id,lesson_type,lesson_name):
    a = les.lessons.get_instance()
    return a.get_lesson(object_id,lesson_type,lesson_name)


@app.route('/api/university/tyt',methods=['GET'])
def search_data():
    name = request.args.get("name")
    location = request.args.get("location")
    max = request.args.get("max",type=int)
    min = request.args.get("min",type=int)
    department = request.args.get("dep")
    uni_type = request.args.get("type")
    a = university_query_generator.query_generator(name,location,max,min,department,uni_type)
    return a.run_query()

@app.route('/api/workout/new_workout',methods=['POST'])
def new_workout():
    json_data = request.get_json()
    a = work_class.workout()
    return a.set_new_workout(json_data)

@app.route('/api/workout/get_workouts/<string:username>',methods=['GET'])
def get_workouts(username):
    a = work_class.workout()
    return a.get_workouts(username)

@app.route('/api/success/get_all_rate',methods=['GET'])
def get_rate():
    a = rate.success_rate()
    return a.get_all_user_rate()


if __name__ == "__main__":
    app.run(debug = True)