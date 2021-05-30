from university import university
from db_university import target_university

db_university = target_university.get_instance()
unv = university.get_instance()

def set_new_target_university(data):
    unv.object_id = data['_id']
    unv.section = data['section']
    unv.target_university = data['target_university']
    unv.target_department = data['target_department']
    unv.target_point = data['target_point']
    return db_university.add_new_target()

def delete_current_target(obj_id):
    return db_university.delete_current_target(obj_id)

def set_university_model(data):
    unv.object_id = data['_id']
    unv.section = data['section']
    unv.target_university = data['target_university']
    unv.target_department = data['target_department']
    unv.target_point = data['target_point']
    return db_university.update_target()

def get_current_target(objectid):
    return db_university.get_current_university_data(objectid)