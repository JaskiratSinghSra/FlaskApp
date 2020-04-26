from flask import Blueprint
from flask_restplus import Api
from flask import Blueprint
from flask_restplus import Resource, Api

blueprint = Blueprint('api', __name__)
api = Api(blueprint)

ns_conf = api.namespace('conferences', description='Conference operations')


@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


@ns_conf.route("/conferences/")
class ConferenceList(Resource):
    def get(self):
        """
        returns a list of conferences
        """

    def post(self):
        """
        Adds a new conference to the list
        """


@ns_conf.route("/conferences/<int:id>")
class Conference(Resource):
    def get(self, id):
        """
        Displays a conference's details
        """

    def put(self, id):
        """
        Edits a selected conference
        """


