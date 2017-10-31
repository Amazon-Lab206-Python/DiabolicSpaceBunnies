
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
import random
app.secret_key = 'ThisisSecret'


@app.route('/index', methods=["POST"]
def info():
   session['form_data']=request.form
    print session['counter']
    return redirect('result.html')

@app.route('/')
def choose number():
       counter=random.randrange(0, 101)
return render_template('index.html', counter=session['counter'])

app.run(debug=True)
