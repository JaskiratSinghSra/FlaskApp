from flask import Blueprint
from flask_restplus import Resource, Api, reqparse

blueprint = Blueprint('api', __name__)
api = Api(blueprint)

ns_conf = api.namespace('user', description='Operations related to user')

user_parser = reqparse.RequestParser()
user_parser.add_argument('email', required=True, help='User Email')


@api.route('/health')
class HelloWorld(Resource):
    def get(self):
        return {'STATUS': 'OK'}


@ns_conf.route("/")
class UserList(Resource):
    def get(self):
        """
        returns a list of all users
        """

    def post(self):
        """
        Adds a new user
        """


@ns_conf.route("/<string:email>")
class User(Resource):
    @api.expect(user_parser)
    def get(self, id):
        """
        Displays a particular user details details
        """

    def put(self, id):
        """
        Edits a selected user
        """


