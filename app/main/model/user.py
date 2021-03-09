from .. import db
from datetime import datetime as dt


class Subscription(db.Model):
    """
    Subscription table
    ### Ancestors
    * flask_sqlalchemy.model.Model

     #Class Attributes
    `email`
    `id'
    `subscription`
    `timestamp`

    constructor:
             # Required Email only
             def __init__(self, email, )
    """

    __tablename__ = "Subscription"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(120), unique=True)
    subscription = db.Column(db.Boolean, unique=False, default=True)
    timestamp = db.Column(db.DateTime, default=dt.now())

    def __init__(self, email, ):
        self.email = email
        self.subscription = True
