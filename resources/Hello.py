from flask_restful import Resource

class Hello(Resource):
    def get(self):
        return {"message": "Hello, get"}


    def post(self):
        return {"message": "Hello, post"}