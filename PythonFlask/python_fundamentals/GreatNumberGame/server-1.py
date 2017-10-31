from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
import random
app.secret_key = 'ThisisSecret'


@app.route('/info', methods=["POST"])
def info():
    session['guess'] = request.form['guess']
    print "guess of {} and randomNumber of {}".format(session['guess'], session['randomNumber'])
    return redirect('/')


@app.route('/')
def chooseNumber():

    # Define guess or default to 0
    guess = 0
    if request.args.get('guess') is not None:
        guess = int(request.args.get('guess'))

    # if there is no random number, create the random number
    if 'randomNumber' not in session:
        session['randomNumber'] = random.randrange(1, 101)

    randomNumber = session['randomNumber']

    # Determine if value is high, low, correct, or not started
    # if there is no guess, we haven't started
    print "guess of {} and randomNumber of {}".format(guess, session['randomNumber'])
    if guess == 0:
        status = 'not_started'
    elif guess > randomNumber:
        status = 'too_high'
    elif guess < randomNumber:
        status = 'too_low'
    else:
        status = 'correct'
        # remove the number so we can have a new number
        session.pop('randomNumber')

    return render_template('index-1.html', status=status)


app.run(debug=True)
