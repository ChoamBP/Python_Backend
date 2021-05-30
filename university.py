class university:

    __instance__ = None

    @staticmethod
    def get_instance():
        if not university.__instance__:
            university()
        return university.__instance__
    
    def __init__(self):
        super().__init__()
        if university.__instance__ is None:
            university.__instance__ = self
        else:
            raise Exception("You cannot create another class")
    
    @property
    def object_id(self):
        return self._object_id
    
    @property
    def section(self):
        return self._section

    @property
    def target_university(self):
        return self._target_university
    
    @property
    def target_department(self):
        return self._target_department
    
    @property
    def target_point(self):
        return self._target_point
    
    @object_id.setter
    def object_id(self,new_object_id):
        self._object_id = new_object_id
    
    @section.setter
    def section(self,new_section):
        self._section = new_section
    
    @target_university.setter
    def target_university(self,new_target_university):
        self._target_university = new_target_university
    
    @target_department.setter
    def target_department(self,new_target_department):
        self._target_department = new_target_department
    
    @target_point.setter
    def target_point(self,new_target_point):
        self._target_point = new_target_point
