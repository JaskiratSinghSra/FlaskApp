from flask import Blueprint
from flask_restplus import Resource, Api

blueprint = Blueprint('api', __name__)
api = Api(blueprint)

ns_conf = api.namespace('user', description='Operations related to user')


@api.route('/health')
class HelloWorld(Resource):
    def get(self):
        return {'STATUS': 'OK'}


@ns_conf.route("/")
class ConferenceList(Resource):
    def get(self):
        """
        returns a list of all users
        """

    def post(self):
        """
        Adds a new user
        """


@ns_conf.route("/<string:email>")
class Conference(Resource):
    def get(self, id):
        """
        Displays a particular user details details
        """

    def put(self, id):
        """
        Edits a selected user
        """


