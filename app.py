from flask import Blueprint
from flask_restful import Api
from resources.Hello import Hello

apiBp = Blueprint('api', __name__)
api = Api(apiBp)

api.add_resource(Hello, '/Hello')