from flask import Blueprint
from flask_restplus import Api
from endpoints.user import api as ns1

blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint,
          title='My Title',
          version='1.0',
          description='A description'
          )

api.add_namespace(ns1)
