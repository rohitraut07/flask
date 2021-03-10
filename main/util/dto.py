from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'id': fields.String(required=False, description='user id'),
        'email': fields.String(required=True, description='user email'),
        'subscription': fields.Boolean(required=False, description='user subscription'),
        'timestamp': fields.DateTime(required=False, description='user Identifier', default=True)
    })