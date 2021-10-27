from D_J_app.config.mysqlconnection import connectToMySQL
from D_J_app.models.ninja import Ninja
from flask import flash

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
    
    @classmethod
    def get_all_ninjas_in_dojo(cls, data):
        query = "SELECT dojos.*, ninjas.* FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(dojo_id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        this_dojo = cls(results[0])
        for ninja in results:
            ninja_data = {
                "id": ninja['ninjas.id'],
                "first_name": ninja['first_name'],
                "last_name": ninja['last_name'],
                "age": ninja['age'],
                "created_at": ninja['created_at'],
                "updated_at": ninja['updated_at'],
                "dojo_id": ninja['dojo_id']
            }
            this_dojo.ninjas.append(Ninja(ninja_data))
        return this_dojo

    @classmethod
    def create(cls, data):
        query = "INSERT INTO dojos(name, created_at, updated_at) VALUES (%(dojo_name)s,NOW(),NOW());"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)

    @staticmethod
    def validate_dojo(dojo):
        is_valid = True # we assume this is true
        if len(dojo['dojo_name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        # if len(dojo['bun']) < 3:
        #     flash("Bun must be at least 3 characters.")
        #     is_valid = False
        # if int(dojo['calories']) < 200:
        #     flash("Calories must be 200 or greater.")
        #     is_valid = False
        # if len(dojo['meat']) < 3:
        #     flash("Bun must be at least 3 characters.")
        #     is_valid = False
        return is_valid
