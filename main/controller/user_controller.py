from flask import request, jsonify
from flask_restplus import Resource

from app.main.util.dto import UserDto
from app.main.service.user_service import subscribe_user, change_subscription

api = UserDto.api
_user = UserDto.user
_update = UserDto.update


@api.route('/subscription')
class InserUser(Resource):
    @api.doc("Insert User")
    @api.marshal_with(_user)
    def post(self):
        """Creates a new User """
        data = request.json
        x = subscribe_user(data=data)
        
        return x

@api.route('/subscription')
class UpdateUser(Resource):
    @api.doc("Update User")
    @api.marshal_with(_update)
    def put(self):
        """Creates a new User """
        data = request.json
        x = change_subscription(data=data)
        print(x)
        return change_subscription(data=data)

