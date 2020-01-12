from flask import Flask,render_template
from flask_bootsrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template(login.html)


@app.route('/signup')
def login():
    return render_template(signup.html)


@app.route('/dashboard')
def login():
    return render_template(dashboard.html)


