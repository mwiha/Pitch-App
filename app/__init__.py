from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
mail = Mail()
db = SQLAlchemy(app)
db.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///site.db"

def create_app(config_name):
    app = Flask(__name__)
    
    mail.init_app(app)
    
    
photos = UploadSet('photos',IMAGES)
def create_app(config_name):
    app = Flask(__name__)
    #........

    # configure UploadSet
    configure_uploads(app,photos)

    #.......