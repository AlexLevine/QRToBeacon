from flask import render_template
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "This is the index page!"

@app.route("/info")
def info():
    return "This is the info page!"

@app.route("/user/<username>")
def show_user(username):
    return "This is " + username + "'s page!"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/bacon/')
def bacon():
    return render_template('bacon.html')

if __name__ == "__main__":
    app.run()
