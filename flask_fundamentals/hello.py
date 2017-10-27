from flask import Flaskapp = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hellow World!'


app.run(debug=True)
