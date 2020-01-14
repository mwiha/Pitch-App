from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .auth import auth as auth_blueprint
from flask_login import LoginManager

app = Flask(__name__)
mail = Mail()
db = SQLAlchemy(app)
db.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///site.db"

def create_app(config_name):
    app = Flask(__name__)
    
    mail.init_app(app)
    
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')
    
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):
    #....
    #Initializing Flask Extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    
    
photos = UploadSet('photos',IMAGES)
def create_app(config_name):
    app = Flask(__name__)
    #........

    # configure UploadSet
    configure_uploads(app,photos)

    #.......