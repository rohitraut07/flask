from flask_restplus import Namespace, fields
from datetime import datetime
 
class UserDto:
    api = Namespace('user', description='user related operations')
    user_model = api.model('UserModel', {
          'id': fields.Integer(required=True, description='user id in database'),
          'mail': fields.String(required=True, description='user mail id'),
          'timeStamp': fields.DateTime(required=True, description='time stamp'),
          'subscribed': fields.Boolean(required=True, description='subscription status'),
    })
    user = api.model('user', {
        'status': fields.Integer(required=True, description='status code'),
        'change': fields.Boolean(required=True, description='change in database') ,
        'new': fields.Boolean(required=True, description='is user in new'),
        'message': fields.String(required=True, description='message'),
        'user':  fields.List(fields.Nested(user_model))
    })
    update = api.model('update', {
        'status': fields.Integer(required=True, description='status code'),
        'change': fields.Boolean(required=True, description='change in database'),
        'message': fields.String(required=True, description='message'),
        'email': fields.String(required=True, description='user mail id')
    })

    #  {
        
    # }
    #  'state': fields.String(required=True, description='user id'),
    #     'email': fields.String(required=True, description='user email'),
    #     'subscription': fields.Boolean(required=True, description='user subscription'),
    #     'timestamp': fields.DateTime(required=True, description='user Identifier',)
    #    'subscription': fields.Boolean(required=True, description='user subscription'),
    