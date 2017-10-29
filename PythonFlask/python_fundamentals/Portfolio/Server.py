from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('home.html')


@app.route('/projects')
def project():
    return render_template('projects.html')


@app.route('/aboutMe')
def portfolio():
    return render_template('aboutMe.html')


app.run(debug=True)
