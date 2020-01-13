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
    
    
 class Registerform(Flaskform):
     email = stringField('email', validators=[InputRequired(), Email(message ='Invalid email'), Length(max-50)])  
     username = stringField('username', validatiors=[InputRequired(), Length(min=4, max=15)])
     password = passwprdField('password', validatiors=[InputRequired(), Length(min=4, max=15)])  


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET','POST'])
def login():
    form =Loginform()
    if form.validate_on_submit():
        return '<h1> "form.username.date +'' + form.password.data + '<h1>"
    return render_template(login.html, form=form)


@app.route('/signup', methods=['GET','POST'])
def login():
    form = Registerform()
    return render_template(signup.html, form=form)


@app.route('/dashboard')
def login():
    return render_template(dashboard.html)


#  