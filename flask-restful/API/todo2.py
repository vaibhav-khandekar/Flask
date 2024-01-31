from flask import Flask
from flask_restful import Resource, Api, reqparse, abort

app = Flask(__name__)
api = Api(app)

todos = {
    1: {"task" : "task 1", "summary" : "learn and upgrade your skills"},
    2: {"task" : "task 2", "summary" : "get a job and kickstart your career"},
    3: {"task" : "task 3", "summary" : "do some aissh in your life"}
}

task_post_args = reqparse.RequestParser()
task_post_args.add_argument("task", type = str, help = "task is required", required = True)
task_post_args.add_argument("summary", type = str, help = "summary is required", required = True)

class Todo(Resource):
    # get API
    def get(self,id):
        return todos[id]

    # post API
    def post(self,id):
        args = task_post_args.parse_args()
        if id in todos:
            abort(409, "task id is already there in the list")
        todos[id] = {"task" : args["task"], "summary" : args["summary"]}
        return todos[id]

class TodoList(Resource):
    # get API
    def get(self):
        return todos

api.add_resource(Todo,'/todo/<int:id>')
api.add_resource(TodoList,'/todo/')

if __name__ == '__main__':
    app.run(debug = True)
