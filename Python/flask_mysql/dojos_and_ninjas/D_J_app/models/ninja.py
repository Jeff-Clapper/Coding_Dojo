from D_J_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']

    @classmethod
    def create(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, created_at,updated_at,dojo_id) VALUES (%(first_name)s,%(last_name)s,%(age)s,NOW(),NOW(),%(dojo_id)s);"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)

    @staticmethod
    def validate_dojo(ninja):
        is_valid = True 
        if int(ninja['dojo_id']) < 1:
            flash("Ninja's must have a dojo.")
            is_valid = False
        if len(ninja['first_name']) < 2:
            flash("First name must contain at least 2 characters.")
            is_valid = False
        if len(ninja['last_name']) < 2:
            flash("Last name must contain at least 2 characters.")
            is_valid = False
        return is_valid