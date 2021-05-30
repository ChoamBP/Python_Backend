from db_tyt_university_query import tyt_university




class query_generator():

    def __init__(self,university_name = None, location = None, max_point = None, min_point = None, department = None, uni_type = None):
        super().__init__()
        self._db_tyt = tyt_university()
        self._university_name = university_name
        self._location = location
        self._max_point = max_point
        self._min_point = min_point
        self._department = department
        self._uni_type = uni_type
        self.query = {"$and":[]}

    def run_query(self):
        self.generate_query_tyt()
        return self._db_tyt.search_university(self.query)

    def generate_query_tyt(self):
        self.check_name()
        self.check_location()
        self.check_max_point()
        self.check_min_point()
        self.check_department()
        self.check_uni_type()

    def check_name(self):
        if not self._university_name == None:
            query = {"universite":self._university_name}
            self.query.get("$and").append(query)
    
    def check_location(self):
        if not self._location == None:
            query = {"sehir":self._location}
            self.query.get("$and").append(query)
    
    def check_max_point(self):
        if not self._max_point == None:
            query = {"tavan_puan":{"$lt":self._max_point}}
            self.query.get("$and").append(query)
    
    def check_min_point(self):
        if not self._min_point == None:
            query = {"taban_puan":{"$gt":self._min_point}}
            self.query.get("$and").append(query)
    
    def check_department(self):
        if not self._department is None:
            query = {"bolum":self._department}
            self.query.get("$and").append(query)
    
    def check_uni_type(self):
        if not self._uni_type is None:
            query = {"universite_turu":self._uni_type}
            self.query.get("$and").append(query)
