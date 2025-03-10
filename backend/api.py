from flask import Flask,request
from flask_restx import Resource, Api

app = Flask(__name__)
api = Api(app,doc="/")


@api.route('/hello')
@api.doc(params={'id':'test'})
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
    

api.add_resource(HelloWorld,'/hello')

if __name__ == '__main__':
    app.run(debug=True)
