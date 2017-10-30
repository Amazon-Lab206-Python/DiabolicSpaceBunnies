from flask import Flask, render_template, request, redirect
import urllib
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/ninja')
def four():
    return render_template('ninja.html')


@app.route('/ninja/<ninja_color>')
def ninja_color(ninja_color):
    return render_template('ninja_color.html', ninja_color=ninja_color)


app.run(debug=True)
