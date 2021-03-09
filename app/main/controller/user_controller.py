import sys, os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + os.sep + '../..')
from flask import request
from flask_restplus import Resource
# import util
from util import dto
from service.user_service import update_user, insert_user

api = UserDto.api
_user = UserDto.user


@api.route('/api/subscription')
class InsertUser(request):
    @api.doc("Insert User")
    @api.marshal_with(_user, envelope='data')
    def post(self):
        """Creates a new User """
        data = request.json
        return insert_user(data=data)


@api.route('/api/subscription')
class InsertUser(request):
    @api.doc("Update User")
    @api.marshal_with(_user, envelope='data')
    def put(self):
        """Creates a new User """
        data = request.json
        return update_user(data=data)
