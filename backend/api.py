from functools import wraps
from Admin.Session import Session
from Admin.User import User
from flask import Flask, abort, request
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app,doc="/")


sessions=[]
user=User()
user.createUser("Test","Test")

def checkAuth(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get("Authentication")
        sess=Session(auth_header)
        if sess.isValid():
            return f(*args, **kwargs, session=sess.getSession())
        else:
            abort(401, "Unauthorized: Invalid or missing authentication token")
    return decorated_function


@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        user=User()
        return {'hello': user.name()}

login_model = api.model('Login',{
    'user': fields.String(
        description='username',
        required=True,        
    ),
    'pass': fields.String(
        description='password',
        required=True,        
    ),
})

session_model = api.model('Session',{
    'id': fields.String(
        description='session id',
        required=True,        
    ),
    'userid': fields.String(
        description='user of session',
        required=True,        
    ),
    'sessionStart': fields.Float(
        description='Start of session timestamp',
        required=True,        
    ),
    'lastAction': fields.Float(
        description='last session action timestamp',
        required=True,        
    ),
    'sessionTime': fields.Float(
        description='session running time',
        required=True,        
    ),
})

@api.route('/login')
class LoginClass(Resource):
    @api.doc(description="Login to get authentication header",responses={401: 'Unauthorized'})
    @api.expect(login_model)
    @api.marshal_with(session_model)
    def post(self):
        data=request.get_json(force=True)
        self.user=User()
        self.user.loginUser(data["user"],data["pass"])
        if self.user.isValid():
            sess=Session("")
            sess.newSession(data['user'])
            return sess.getSession() 
        else:
            abort(401,"Unauthorized: Invalid or missing credentials")
    
@api.route('/status')
class StatusClass(Resource):
    @checkAuth
    def get(self,session):
        return session 



if __name__ == '__main__':
    app.run(debug=True)
