from datetime import datetime
from app.main import db
from app.main.model.user import Subscription
from flask import jsonify


def subscribe_user(data):
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
    user = Subscription.query.filter_by(email=data['email']).first()
    if not user:
        user = Subscription(data['email'])
        db.session.add(user)
        db.session.commit()
        # app.logger.info('%s : successfully subscribed', user.email)
        status =  201
        change = True
        new = True
        message = 'user added to database'
        user = {
                'id': user.id,
                'mail': user.email,
                'timeStamp': user.timestamp,
                'subscribed': user.subscription
                }
    else:
        # app.logger.info('%s : User already exist', user.email)
        status = 200
        change = False
        new = False
        message = 'User already exist in database'
        user = {
                'id': user.id,
                'mail': user.email,
                'timeStamp': user.timestamp,
                'subscribed': user.subscription
        }
    return {
        'status': status,
        'change': change,
        'new': new,
        'message': message,
        'user': user
    }
    
def change_subscription(data):
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
    update_this = Subscription.query.filter_by(email=data['email']).first()
    if update_this:
        update_this.subscription = not update_this.subscription
        update_this.timestamp =datetime.now()
        db.session.commit()
        # app.logger.warning('%s : Subscription Changed', data['email'])
        status = 200
        change = True
        message = 'Subscription changed'
        email = update_this.email
    else:
        # app.logger.warning('%s : User not exist', data['email'])
        status = 404
        change = True
        message = 'User not exist'
        email = data['email']

    return {
        'status': status,
        'change': change,
        'message': message,
        'email': email
    }
