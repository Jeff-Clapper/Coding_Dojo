from flask_appie import app
from flask import  render_template, redirect, request
from flask_appie.models.user import User

@app.route('/')
def home():
    users = User.get_all()
    return render_template("index.html", users = users)

@app.route('/create')
def create():
    return render_template("create.html")

@app.route('/submit', methods=['POST'])
def submit():
    data = {
        "fname": request.form['fname'],
        "lname": request.form['lname'],
        "email": request.form['email']
    }
    User.create(data)
    return redirect('/')

@app.route('/show/<int:user_id>')
def show(user_id):
    data = {
        'id':user_id
    }
    results = User.get_user(data)
    print(results)
    return render_template('show.html', person = results[0] )

@app.route('/delete/<int:user_id>')
def delete_user(user_id):
    data = {
        'id':user_id
    }
    User.delete_user(data)
    return redirect('/')

@app.route('/edit/<int:user_id>')
def edit(user_id):
    id = user_id
    return render_template('edit.html', id = id)

#MUST CHANGE THIS
@app.route('/update/<int:user_id>', methods=['POST'])
def update(user_id):
    data = {
        'id': user_id,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.update_user(data)
    return redirect('/')
