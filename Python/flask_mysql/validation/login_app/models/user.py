from flask.globals import request
from login_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

name_regex = re.compile(r'^[a-zA-Z]+$')
email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def register(cls,data):
        query = "INSERT INTO users(first_name,last_name,email,password,created_at,updated_at) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s,NOW(),NOW());"
        return connectToMySQL('login_schema').query_db(query,data)
        
    @classmethod
    def login(cls,data):
        query = 'SELECT * FROM users WHERE email = %(email)s'
        results = connectToMySQL('login_schema').query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def user_page(cls,data):
        query = 'SELECT * FROM users WHERE id = %(id)s'
        results = connectToMySQL('login_schema').query_db(query,data)
        return cls(results[0])
    
    @staticmethod
    def password_compare(pw1,pw2):
        if len(pw1) < 8:
            flash('Passwords must be a mininum of 8 characters.')
            return False
        elif pw1 != pw2:
            flash('Passwords must match.')
            return False
        else:
            return True
        
    @staticmethod
    def registration_validation(data):
        is_valid = True
        query = 'SELECT id FROM users where email = %(email)s'
        results = connectToMySQL('login_schema').query_db(query,data)
        if len(results) > 0:
            flash('This email is already exists.')
            is_valid = False
            return is_valid
        if (len(data['first_name']) < 2) or (len(data['last_name']) < 2):
            flash('first and last name must be at least two letters long.')
            is_valid = False
        if not name_regex.match(data['first_name']):
            flash("First name should be only letters.")
            is_valid = False
        if not name_regex.match(data['last_name']):
            flash("Last name should be only letters.")
            is_valid = False
        if not email_regex.match(data['email']):
            flash('Please use a valid email address.')
            is_valid = False
        if data['password'] == False:
            is_valid = False
        return is_valid

    @staticmethod
    def login_validation(email):
        is_valid = True
        if not email_regex.match(email):
            is_valid = False
        return is_valid
