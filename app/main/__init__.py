from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from .config import config_by_name

db = SQLAlchemy()
flask_bcrypt = Bcrypt()


def create_app(config_name):
    fapp = Flask(__name__)
    fapp.config.from_object(config_by_name[config_name])
    db.init_app(fapp)
    flask_bcrypt.init_app(fapp)
    return fapp
