from flask import Flask,render_template, request, session, redirect,flash
from mysqlconnection import connectToMySQL

app = Flask(__name__)
app.secret_key = 'This is a secret key. Secret secret secret'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def users():
    session['username'] = request.form['name']
    session['userdojo'] = request.form['dojo_location']
    session['userlanguage'] = request.form['language']
    session['usercomments'] = request.form['comments']
    return redirect('/results')

@app.route('/results')
def results():
    return render_template('results.html', location=session['userdojo'],language=session['userlanguage'],comments=session['usercomments'])

@app.route('/home', methods=['POST'])
def goHome():
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)