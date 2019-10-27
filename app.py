from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

tasks = [
    {
        "id": 1,
        "title": "Get task",
        "description": "Create RestAPI for get task",
        "done": False
    },
    {
        "id": 2,
        "title": "Create task",
        "description": "Create RestAPI for create task",
        "done": False
    }
]


class Tasks(Resource):
    def get(self, id = 0):
        if id == 0:
            return tasks, 200

        for task in tasks:
            if task["id"] == id:
                return task, 200

        return "Task not found", 404


    def post(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("title")
        parser.add_argument("description")
        params = parser.parse_args()

        for task in tasks:
            if id == task["id"]:
                return f"Task with id {id} already exists", 400
            
        task = {
            "id": int(id),
            "title": params["title"],
            "description": params["description"],
            "done": False
        }

        tasks.append(task)

        return task, 201


    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("title")
        parser.add_argument("description")
        parser.add_argument("done")
        params = parser.parse_args()

        for task in tasks:
            if id == task["id"]:
                task["title"] = params["title"]
                task["description"] = params["description"]
                task["done"] = bool(params["done"])

                return task, 200

        task = {
            "id": id,
            "title": params["title"],
            "description": params["description"],
            "done": params["done"]
        }

        tasks.append(task)

        return task, 201


    def delete(self, id):
        global tasks
        tasks = [task for task in tasks if task["id"] != id]

        return f"Task with id {id} is deleted.", 200


api.add_resource(Tasks, '/tasks', '/tasks/', '/tasks/<int:id>')
if __name__ == '__main__':
    app.run(debug=True)