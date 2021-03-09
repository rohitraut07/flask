from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('subscriber', description='user related operations')
    user = api.model('subscriber', {
        'id': fields.String(required=False, description='user id'),
        'email': fields.String(required=True, description='user email address'),
        'subscription': fields.String(required=False, description='user subscription state'),
        'timestamp': fields.String(required=False, description='timestamp'),
    })
