class user:

    __instance__ = None

    @staticmethod
    def get_instance():
        if not user.__instance__:
            user()
        return user.__instance__
    
    def __init__(self):
        super().__init__()
        if user.__instance__ is None:
            user.__instance__ = self
        else:
            raise Exception("You cannot create another class")
    

    @property
    def object_id(self):
        return self._object_id

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password
    
    @property
    def name(self):
        return self._name
    
    @property
    def email(self):
        return self._email
    
    @property
    def profile_picture_url(self):
        return self._profile_picture_url
    
    @property
    def gender(self):
        return self._gender
        
    @property
    def user_class(self):
        return self._user_class

    @object_id.setter
    def object_id(self,new_object_id):
        self._object_id = new_object_id    

    @username.setter
    def username(self,new_username):
        self._username = new_username
    
    @password.setter
    def password(self,new_password):
        self._password = new_password
    
    @name.setter
    def name(self,new_name):
        self._name = new_name
    
    @email.setter
    def email(self,new_email):
        self._email = new_email
    
    @profile_picture_url.setter
    def profile_picture_url(self,new_profile_picture_url):
        self._profile_picture_url = new_profile_picture_url
    
    @gender.setter
    def gender(self,new_gender):
        self._gender = new_gender
    
    @user_class.setter
    def user_class(self,new_user_class):
        self._user_class = new_user_class