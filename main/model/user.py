from .. import db, flask_bcrypt
from datetime import datetime

class Subscription(db.Model):
    """ User Model for storing user related details """

    __tablename__ = "subscribers"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(120), unique=True)
    subscription = db.Column(db.Boolean, unique=False, default=True)
    timestamp = db.Column(db.DateTime, default=datetime.now())
    
    def __init__(self,email):
        self.email = email