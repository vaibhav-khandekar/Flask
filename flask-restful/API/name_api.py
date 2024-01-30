from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello':'world'}

class HelloName(Resource):
    def get(self,name):
        return {'data':'hello {}'.format(name)}

api.add_resource(HelloWorld,'/')
api.add_resource(HelloName,'/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)
