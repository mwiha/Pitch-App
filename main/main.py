from flask import Flask,render_template
from flask_bootsrap import Bootstrap
from fask_wtf import Flaskform 
from wtforms import stringField,Booleanfield
from wtforms.validatiors import InputRequired,Email,Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissuppossedtobesecret!'
Bootstrap(app)

class Loginforms(Flaskform):
    username = stringField('username', validatiors=[InputRequired(), Length(min=4, max=15)])
    password = passwprdField('password', validatiors=[InputRequired(), Length(min=4, max=15)])
    remember =Booleanfield('remember me')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    form =Loginform()
    return render_template(login.html, form=form)


@app.route('/signup')
def login():
    return render_template(signup.html)


@app.route('/dashboard')
def login():
    return render_template(dashboard.html)


#  