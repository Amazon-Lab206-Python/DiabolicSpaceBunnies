from flask import Flask, render_template, request, redirect
import urllib
app = Flask(__name__)


@app.route('/', methods=['POST'])
def signup():
    print "Fill out the form"
    name = request.form['name']
    email = request.form['email']
    print "sign up for our emails {}".format(request.form)
    # form on home page
    return redirect('/process?name=' + urllib.quote_plus(name))


@app.route('/')
def root():
    # this gives us the home page when we land on it
    return render_template('index.html')


@app.route('/process')
def success():
    name = request.args.get('name')
    # directs us to success message
    return render_template('process.html', name=name)


app.run(debug=True)
