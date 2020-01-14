from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail


mail = Mail()

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