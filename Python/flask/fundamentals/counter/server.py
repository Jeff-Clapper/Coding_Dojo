from flask import Flask, session, render_template, request, redirect

app = Flask(__name__)
app.secret_key = 'This is a secret key. Secret secret secret'

@app.route('/')
def home():
    if 'visits' in session:
        session['visits'] += 1
    else:
        session['visits'] = 1
    if 'total_visits' in session:
        session['total_visits'] += 1
    else:
        session['total_visits'] = 1
    return render_template('index.html',total_visits = session['total_visits'],visits = session['visits'])

@app.route('/doubleCount', methods=['POST'])
def doubleCount():
    session['total_visits'] +=1
    session['visits'] +=1
    return redirect('/')

@app.route('/destroy')
def destroy():
    if session['visits'] == 1:
        session.clear()
    else:
        session.pop('visits')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
