import re
from login_app import app
from flask import render_template, redirect, request, flash, session
from login_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/register',methods=['POST'])
def register_user():
    pw1 = request.form['password']
    pw2 = request.form['confirm_password']
    results = User.password_compare(pw1,pw2)
    if not results:
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': results  
        }
    else:
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': bcrypt.generate_password_hash(request.form['password'])
        }
    if not User.registration_validation(data):
        return redirect('/')
    else:
        User.register(data)
        session['email'] = data['email']
        return redirect('/register/login') 

@app.route('/register/login')
def login_from_registration():
    user = User.login({'email':session['email']})
    return render_template('user_page.html', user = user)


@app.route('/login',methods=['POST'])
def login():
    email = request.form['email']
    if not User.login_validation(email):
        flash('Invalid username/password')
        return redirect ('/')
    else:
        data = {'email':email}
    user = User.login(data)
    if not user:
        flash('Invalid username/password')
        return redirect ('/')
    if not bcrypt.check_password_hash(user.password,request.form['password']):
        flash('Invalid username/password')
        return redirect ('/')
    session['id'] = user.id
    return redirect('/user_page')

@app.route('/user_page')
def users_page():
    user = User.user_page({'id':session['id']})
    return render_template('user_page.html',user = user)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')