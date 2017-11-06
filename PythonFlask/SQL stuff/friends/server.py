from flask import Flask, request, redirect, render_template, session, flash
import datetime
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'friendsdb')


@app.route('/')
def index():
    all_friends = mysql.query_db("SELECT * FROM friends")
    return render_template('index.html', all_friends=all_friends)


@app.route('/friends', methods=['POST'])
def create():
    # add a friend to the database!
    print 'request form {}'.format(request.form)
    name = request.form['name']
    age = request.form['age']
    print mysql.query_db("insert into friends (name, age, friend_since) values ('{}', '{}', '{}')".format(name, age, formattedNowTime()))
    # print mysql.query_db("SELECT * FROM friends")
    return redirect('/')


def formattedNowTime():
    now = datetime.datetime.now()
    timeFormat = '%Y-%m-%d %H:%M:%S'
    formattedTime = now.strftime(timeFormat)
    return formattedTime


print mysql.query_db("SELECT * FROM friends")
app.run(debug=True)
