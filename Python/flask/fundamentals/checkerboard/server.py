from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def checkerBoard8():
    return render_template('index.html',x=int(8),y=int(8),color1='wheat',color2='black',width=640)

@app.route('/4')
def checkerBoard4():
    return render_template('index.html',x=int(8),y=int(4),color1='wheat',color2='black',width=640)

@app.route('/<int:x>/<int:y>')
def checkerBoardXY(x,y):
    return render_template('index.html',x=x,y=y,color1='wheat',color2='black',width=80*x)

@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def colorCheckerBoardXY(x,y,color1,color2):
    return render_template('index.html',x=x,y=y,color1=color1,color2=color2,width=80*x)

if __name__ == '__main__':
    app.run(debug=True)
