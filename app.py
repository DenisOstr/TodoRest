from flask import Flask, jsonify
from flask import make_response, abort

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': 'first task',
        'description': 'complete first task',
        'done': False
    },
    {
        'id': 2,
        'title': 'second task',
        'description': 'complete second task',
        'done': False
    }
]

@app.route('/todo/api/v1.0/tasks/<int:taskId>', methods = ['GET'])
def getTasks(taskId):
    task = [task for task in tasks if task['id'] == taskId]

    if len(task) == 0:
        abort(404)

    return jsonify({ 'tasks': tasks[0] })


@app.errorhandler(404)
def notFound(error):
    return make_response(jsonify( {'error': 'Not Found'} ), 404)


if __name__ == '__main__':
    app.run(debug=True)