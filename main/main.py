from flask import Flask,render_template,redirect,url for
from flask_bootsrap import Bootstrap
from fask_wtf import Flaskform 
from wtforms import stringField,Booleanfield
from wtforms.validatiors import InputRequired,Email,Length
from flask_sqlalchemy import SQLALchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissuppossedtobesecret!'
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:////mnt/c/users/alice/Documents/login-example/ database.db'
Bootstrap(app)
db =SQLALchemy (app)

class user(db,model):
    id =db.column(db.Integer,primary_key=True)
    username =db.column(db.string(15),unique=True)
    email =db.column(db.string(50),unique=True)
    password =db.column(db.string(80))

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
        user =user.query.filter_by(username=form.username.data).first()
        if user:
            if user.password == form.passwprd.data:
                return redirect(url_for('dashboard'))
            
            
        # return '<h1> "form.username.date +'' + form.password.data + '<h1>"
    return render_template(login.html, form=form)


@app.route('/signup', methods=['GET','POST'])
def login():
    form = Registerform()
    
    if form.validate_on_submit():
        new_user = user( username =form.username.data, email=form.email.data,password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        
        return '<h1>New user has been created!'
        # return '<h1> "form.username.date +'' + form.email.data+ '' + form.password.data + '<h1>"
    return render_template(signup.html, form=form)


@app.route('/dashboard')
def login():
    return render_template(dashboard.html)


#  