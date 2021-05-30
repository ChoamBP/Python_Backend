from user import user
from db_profile import profile

db_profile = profile.get_instance()
usr = user.get_instance()

def set_new_profile_model(data):
    usr.username = data['username']
    usr.password = data['password']
    usr.name = data['name']
    usr.email = data['email']
    usr.profile_picture_url = data['profile_picture_url']
    usr.gender = data['gender']
    usr.user_class = data['education_class']
    return db_profile.add_new_user()

def delete_user(objectid):
    return db_profile.delete_user_by_id(objectid)

def set_profile_model(data):
    usr.object_id = data['_id']
    usr.username = data['username']
    usr.password = data['password']
    usr.name = data['name']
    usr.email = data['email']
    usr.profile_picture_url = data['profile_picture_url']
    usr.user_class = data['education_class']
    return db_profile.update_user()

def user_exist_check(username,password):
    return db_profile.check_existing(username,password)

def get_all_users():
    return db_profile.get_all_users_data()

def get_user_profile(username):
    return db_profile.check_username(username)