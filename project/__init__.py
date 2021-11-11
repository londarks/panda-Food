from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from .models.model import configure as config_db
from .models.serealizer import configure as config_ma
import os, pathlib

def create_app():
    _DIR = (str(os.path.dirname(pathlib.Path(__file__).parent.absolute())))
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '0MBuF7775NGx_'
    #app.secret_key = '0MBuF7775NGx_'
    app.config["JWT_SECRET_KEY"] = "0MBuF5NGx_"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////{}/migrations/panda.db'.format(_DIR)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    config_db(app=app)
    
    config_ma(app=app)
    
    JWTManager(app)
    
    Migrate(app,app.db)
    
    from .route.routes import pages
    app.register_blueprint(pages)
    
    from .route.admin import admin
    app.register_blueprint(admin)
    
    return app