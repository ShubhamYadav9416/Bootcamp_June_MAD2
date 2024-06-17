from flask import Flask
from flask_restful import Api
import application.config as config

from application.data.database import db
from application.data.models import *

from application.apis.movie.moviesAPI import AllMovieAPI,MovieAPI


app = Flask(__name__)
app.config.from_object(config)
app.app_context().push()


db.init_app(app)

api = Api(app)
api.init_app(app)


api.add_resource(AllMovieAPI, "/api/movie")
api.add_resource(MovieAPI, "/api/movie/<int:movie_id>")


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host="localhost", port=8081, debug = True)
