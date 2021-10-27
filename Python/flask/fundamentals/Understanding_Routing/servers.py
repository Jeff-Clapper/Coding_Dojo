from flask import Flask,render_template

app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template("yellow-belt.html")

@app.route('/dojo')
def dojo():
    return 'Dojo'

@app.route('/<string:name>')
def hello(name):
    return 'Hello '+ name

@app.route('/<int:multiplier>/<string:name>')
def multipleHello(multiplier,name):
    return ('Hello '+ name +'\n')*multiplier 

#EXCEPTION HANDLER EXAMPLE HERE!!!
@app.errorhandler(404)
def page_not_found(e):
    return 'Sorry, no response found'

if __name__ == "__main__":
    app.run(debug=True)