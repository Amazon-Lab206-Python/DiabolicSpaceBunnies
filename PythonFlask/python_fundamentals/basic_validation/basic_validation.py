from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'


@app.route('/')
def index():
    return render_template('basic_validation_index.html')


@app.route('/process', methods=['Post'])
def process():
    # do some validations here!
    if len(request.form['name']) < 1:
        flash("sorry, you gotta have a name")
    else:
        flash("yay, thank you {}".format(request.form['name']))

    return redirect('/')


app.run(debug=True)
