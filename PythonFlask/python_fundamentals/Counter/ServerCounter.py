from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisisSecret'


@app.route('/')
def index():
    try:
        session['counter']
    except:
        session['counter'] = 0

    return render_template('index.html', session['counter'])


app.run(debug=True)
