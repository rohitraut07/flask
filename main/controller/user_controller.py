from flask import request
from flask_restplus import Resource

from app.main.util.dto import UserDto
from app.main.service.user_service import subscribe_user, change_subscription

api = UserDto.api
_user = UserDto.user


@api.route('/api/subscription')
class insert_user(Resource):
    @api.doc("Insert User")
    @api.marshal_with(_user, envelope='data')
    def post(self):
        """Creates a new User """
        data = request.json
        return subscribe_user(data=data)

@api.route('/api/subscription')
class update_user(Resource):
    @api.doc("Update User")
    @api.marshal_with(_user, envelope='data')
    def put(self):
        """Creates a new User """
        data = request.json
        return change_subscription(data=data)

