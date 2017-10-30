from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisisSecret'


@app.route('/')
def index():
    try:
        session['counter'] += 1
    except:
        session['counter'] = 0

    return render_template('result.html', counter=session['counter'])


@app.route('/info', methods=["POST"])
def info():
    session['counter'] += 1
    print session['counter']
    return redirect('result.html')


app.run(debug=True)
