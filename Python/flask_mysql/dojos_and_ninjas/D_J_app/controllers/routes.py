from D_J_app import app
from flask import render_template, redirect, request, flash
from D_J_app.models.dojo import Dojo
from D_J_app.models.ninja import Ninja

@app.route('/')
def home():
    dojos = Dojo.get_all()
    return render_template('home.html', dojos = dojos)

@app.route('/new_ninja')
def new_ninja():
    dojos = Dojo.get_all()
    return render_template('new_ninja.html', dojos = dojos)

@app.route('/dojo/<int:dojo_id>')
def show(dojo_id):
    data = {
        'dojo_id':dojo_id
    }
    this_dojo = Dojo.get_all_ninjas_in_dojo(data)
    return render_template('dojo_roster.html',this_dojo = this_dojo)

@app.route('/create_dojo',methods=['POST'])
def new_dojo():
    data = {
        'dojo_name': request.form['dojo_name']
    }
    if not Dojo.validate_dojo(data):
        return redirect('/')
    else:   
        Dojo.create(data)
    return redirect('/')

@app.route('/create_ninja', methods = ['POST'])
def create_new_ninja():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': int(request.form['age']),
        'dojo_id': request.form['dojo']
    }
    if not Ninja.validate_dojo(data):
        return redirect('/new_ninja')
    else:   
        Ninja.create(data)
        return redirect('/')