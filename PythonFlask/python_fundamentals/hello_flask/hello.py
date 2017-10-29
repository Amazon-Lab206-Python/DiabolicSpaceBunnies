from flask import Flask  # Import Flask to allow us to create our app.
# Global variable __name__ tells Flask whether or not we are running the file
app = Flask(__name__)
# directly, or importing it as a module.


# The "@" symbol designates a "decorator" which attaches the following
@app.route('/')
# function to the '/' route. This means that whenever we send a request to
# localhost:5000/ we will run the following "hello_world" function.
def hello_world():
    # Return the string 'Hello World!' as a response.
    return 'Hello World! <br> My name is bunneh!'


app.run(debug=True)      # Run the app in debug mode.

'''
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template(index.html)


app.run(debug=True)
 @app.route('/success')
 def success():
     return render_template('success.html')'''
