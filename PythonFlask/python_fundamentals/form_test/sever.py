from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("form_test.html")


@app.route('/users', methods=['POST'])
def create_user():
    print "Got Post Info"
    name = request.form['name']
    email = request.form['email']
    print "route create_users with request {}".format(request.form)
    return redirect('/')


app.run(debug=True)
