from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/users/<username>/<id>')
def show_user_profile(username, id):
    print username
    print id
    return render_template("users.html", username=username, id=id)


@app.route('/')
def hiBunny():
    return render_template("indexHiBunny.html", phrase="hi bunny", times=500)


app.run(debug=True)
