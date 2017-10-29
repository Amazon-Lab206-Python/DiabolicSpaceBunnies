from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def greeting():
    return render_template('index.html')


@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')


@app.route('/dojo_form')
def dojo_form():
    return render_template('dojo_form.html')


@app.route('/dojo', methods=['POST'])
def signup_suer():
    print "Fill out the form"
    name = request.form['name']
    email = request.form['email']
    print "sign up for our emails {}".format(request.form)
    return redirect('/')


app.run(debug=True)
