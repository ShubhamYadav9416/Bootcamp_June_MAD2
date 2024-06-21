from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS

import application.config as config

from application.data.database import db
from application.data.models import *
from application.security import security, user_datastore


from application.apis.movie.moviesAPI import AllMovieAPI,MovieAPI
from application.apis.auth.registerAPI import RegisterAPI
from application.apis.auth.loginAPI import LoginAPI, RefreshTokenAPI


app = Flask(__name__)
app.config.from_object(config)
app.app_context().push()

CORS(app, supports_credentials=True)

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET, PUT, POST, DELETE, OPTIONS'

    return response

@app.after_request
def after_request(response):
    response = add_cors_headers(response)
    return response





db.init_app(app)

api = Api(app)
api.init_app(app)

JWTManager(app)

security.init_app(app, user_datastore)

api.add_resource(RegisterAPI, "/api/register")
api.add_resource(LoginAPI,"/api/login")
api.add_resource(RefreshTokenAPI, "/api/refresh_token")
api.add_resource(AllMovieAPI, "/api/movie")
api.add_resource(MovieAPI, "/api/movie/<int:movie_id>")

def creating_roles_initially():
    if Roles.query.filter_by(name = 'watcher').first() is None:
        add_user = Roles(name="watcher", description = "Normal User")
        db.session.add(add_user)
    if Roles.query.filter_by(name = 'admin').first() is None:
        add_lib = Roles(name="admin", description = "Admin")
        db.session.add(add_lib)
    db.session.commit()



with app.app_context():
    db.create_all()
    creating_roles_initially()

if __name__ == "__main__":
    app.run(host="localhost", port=8081, debug = True)
