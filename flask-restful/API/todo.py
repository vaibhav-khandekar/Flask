from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = {
    1: {"task" : "task 1", "summary" : "learn and upgrade your skills"},
    2: {"task" : "task 2", "summary" : "get a job and kickstart your career"},
    3: {"task" : "task 3", "summary" : "do some aissh in your life"}
}

class Todo(Resource):
    def get(self,id):
        return todos[id]

class TodoList(Resource):
    def get(self):
        return todos

api.add_resource(Todo,'/todo/<int:id>')
api.add_resource(TodoList,'/todo/')

if __name__ == '__main__':
    app.run(debug = True)
