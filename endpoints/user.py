from flask_restplus import Namespace, Resource, Api, reqparse
# from domain.user import save_user

api = Namespace('user', description='Operations related to user')


get_user_parser = reqparse.RequestParser()
get_user_parser.add_argument('email', required=True, help='User Email')

add_user_parser = reqparse.RequestParser()
add_user_parser.add_argument('username', required=True, help='Username')
add_user_parser.add_argument('email', required=True, help='User Email')


@api.route('/health')
class HelloWorld(Resource):
    def get(self):
        return {'STATUS': 'OK'}


@api.route("/")
class UserList(Resource):
    def get(self):
        """
        returns a list of all users
        """

    @api.expect(add_user_parser)
    def post(self):
        """
        Adds a new user
        """

        args = add_user_parser.parse_args()
        username = args.username
        email = args.email
        return username


@api.route("/<string:email>")
class User(Resource):
    @api.expect(get_user_parser)
    def get(self, id):
        """
        Displays a particular user details details
        """

    def put(self, id):
        """
        Edits a selected user
        """
