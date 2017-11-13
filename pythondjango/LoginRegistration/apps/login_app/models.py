# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
   password=models.CharField(max_length=255)

def index():
    return render_template('index.html')


def register():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    c_password = request.form['c_password']

     errors = False

    if len(first_name) == 0:
        flash('First Name is required')
        errors = True
    elif not first_name.isalpha():
        flash('First Name can only contain letters')
        errors = True
    if len(last_name) == 0:
        flash('Last Name is required')
        errors = True
    elif not last_name.isalpha():
        flash('Last Name can only contain letters')
        errors = True
    if len(email) == 0:
        flash('Email is required')
        errors = True
    elif not EMAIL_REGEX.match(email):
        flash('Invalid Email')
        errors = True
    if len(password) == 0:
        flash('Password is required')
        errors = True
    elif len(password) < 8:
        flash('Password must be at least 8 characters')
        errors = True
    if len(c_password) == 0:
        flash('Password Confirmation is required')
        errors = True
    elif password != c_password:
        flash('Passwords must match')
        errors = True
    if errors:
        return redirect('/')

    # see if there's an existing email
    query = "SELECT*FROM users WHERE email= :email LIMIT1"
    data = {
        'email': email  # What is the purpose of this line?
    }
    users = mysql.query_db(query, data)
    if len(users) > 0:
        flash('Email already taken')
        return redirect('/')

    query = "INSERT INTO users(first_name, last_name, email, password, created_at, updated_at) VALUES(: first, : last, : email, : password, NOW(), NOW())"
    data = {
        'first': first_name,
        'last': last_name,
        'email': email,
        'password': bcrypt.generate_password_hash(password)
    }

    user_id = mysql.query_db(query, data)
    session['user_id'] = user_id

    return redirect('/success')

def login():
    email = request.form['email']
    password = request.form['password']

    # Check users table for existing user with that email
    query = "SELECT * FROM users WHERE email= :email LIMIT 1"
    data = {
        'email': email
    }
    users = mysql.query_db(query, data)
    if len(users) > 0:
        user = users[0]
        if bcrypt.check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            return redirect('success')
        else:
            flash('Invalid email/Password combo')
            return redirect('/')
    else:
        flash('Invalid email/Password combo')
        return redirect('/')
def success():
        return render_template('succes.html')

def logout():
        session.clear()
    return redirect('/')

