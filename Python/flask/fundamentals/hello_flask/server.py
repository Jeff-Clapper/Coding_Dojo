from flask import Flask,render_template

app = Flask(__name__)
@app.route('/')
def hello_world():
    return "hello_world!"

@app.route('/hello/<string:name>/<int:multiplier>')
def hello(name,multiplier):
    return render_template("hello_you.html", name = name, multiplier = multiplier)

@app.route('/lists')
def render_lists():
    sibling_info = [
        {'name' : 'Jeff', 'age' : '29'},
        {'name' : 'Sarah', 'age' : '27'},
        {'name' : 'Shawn', 'age' : '26'},
        {'name' : 'Emma', 'age' : '22'},
        {'name' : 'Michael', 'age' : '18'}
    ]
    return render_template("lists.html",random_numbers = [8,6,7,5,3,0,9], siblings = sibling_info)

if __name__ == "__main__":
    app.run(debug=True)

