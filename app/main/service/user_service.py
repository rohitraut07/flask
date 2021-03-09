from datetime import datetime as dt

from flask import request

from main import db
from main.model.user import Subscription
from manage import fapp


def insert_user():
    """
    Input:
        Type: json
        example: {
                    "email": "example@gmail.com"
                 }

    Operation:
            1. add log  in log file
                  example@eail.com added to database
                  User already exist in database
            2. Add email in Database if not exist
            3. return info of email if exist in Database
    """
    data = request.get_json()
    user = Subscription.query.filter_by(email=data['email']).first()
    if not user:
        user = Subscription(data['email'])
        db.session.add(user)
        db.session.commit()
        fapp.logger.info('%s : successfully subscribed', user.email)
        response_object = {
            'change': 'true',
            'new': 'true',
            'details': {
                'message': 'User added to database'
            }
        }
        return response_object, 201
    else:
        fapp.logger.info('%s : User already exist', user.email)
        response_object = {
            'user': {
                'id': user.id,
                'mail': user.email,
                'timeStamp': user.timestamp,
                'subscribed': user.subscription
            },
            'status': 409,
            'change': False,
            'new': False,
        }
        return response_object, 409


def update_user():
    """
    Input:
       Type: Json
       Example:
             {
                'email': "example@gmail.com"
             }
    Operation:
         1. Add logs in log file either
                    i. subscription changed
                    ii. user not exist in database
         2. Change Subscription Status<boolean> in database if email exist in database
         3. return user not exist with status code 404 if email not exist in database
    """
    data = request.get_json()
    update_this = Subscription.query.filter_by(email=data['email']).first()
    if update_this:
        update_this.subscription = not update_this.subscription
        update_this.timestamp = dt.now()
        db.session.commit()
        fapp.logger.warning('%s : Subscription Changed', data['email'])
        response_object = {
            'change': 'true',
            'new': 'false',
            'details': {
                'message': 'subscription changed'
            }
        }
        return response_object, 200
    else:
        fapp.logger.warning('%s : User not exist', data['email'])
        response_object = {
            'change': False,
            'new': None,
            'details': {
                'message': 'User not exist'
            }
        }
        return response_object, 404
