from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def nothing():
    return 'Nothing to see here. Go to localhost:5000/play'

@app.route('/play')
def threeBox(num=3,color='cornflowerblue'):
    return render_template('box.html',num = num, color = color)

@app.route('/play/<int:num>')
def xBox(num, color = 'cornflowerblue'):
    return render_template('box.html',num = num, color = color)

@app.route('/play/<int:num>/<string:color>')
def ColorXBox(num,color):
    return render_template('box.html',num = num, color = color)

@app.errorhandler(404)
def pickDifferentColor():
    return 'The color you have chosen is not recognized. Please choose again'

if __name__ == '__main__':
    app.run(debug=True)