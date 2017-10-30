from flask import Flask, render_template, redirect, request
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("WhatsmynameAns.html")


@app.route("/process", methods=['POST'])
def process_form():
    print request.form
    return redirect("/")


app.run(debug=True)
