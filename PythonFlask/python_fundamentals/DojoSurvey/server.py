from flask import Flask, render_template, request, redirect
import urllib
app = Flask(__name__)


@app.route('/', methods=['POST'])
def signup():
    print "Fill out the form"
    print request.form
    name = request.form['name']
    email = request.form['email']
    location = request.form['location']
    favorite_food = request.form['favorite_food']
    comment = request.form['comment']

    # form on home page
    return render_template('process.html', name=name, email=email, location=location, favorite_food=favorite_food, comment=comment)
# REMEMBER TO PASS IN ALL THE VARIABLES
    # return redirect('/process?name=' + urllib.quote_plus(name))


@app.route('/')
def root():
    # this gives us the home page when we land on it
    return render_template('index.html')


# @app.route('/process')
# def success():
#     name = request.args.get('name')
#     # directs us to success message
#     return render_template('process.html', name=name)


app.run(debug=True)
