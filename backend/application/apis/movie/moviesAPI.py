import json
from flask import request, jsonify
from flask_restful import Resource, reqparse, abort, fields, marshal_with

from application.data.models import db,Movie

movie_post_args = reqparse.RequestParser()
movie_post_args.add_argument('movie_name',type=str, required = True,help = "movie name is required" )
movie_post_args.add_argument('movie_lang',type=str, required = True, help = "movie language is required")
movie_post_args.add_argument('movie_duration',type=str, required = True, help = "movie duration is required")
movie_post_args.add_argument('movie_tag',type=str, required = True, help = "movie tag is required")


movie_put_args = reqparse.RequestParser()
movie_put_args.add_argument('movie_name',type=str)
movie_put_args.add_argument('movie_lang',type=str)
movie_put_args.add_argument('movie_duration',type=str)
movie_put_args.add_argument('movie_tag',type=str)

resource_feilds = {
    'movie_id' : fields.Integer,
    'movie_name' : fields.String,
    'movie_tag' : fields.String,
    'movie_lang' : fields.String,
    'movie_duration' : fields.String
}

class AllMovieAPI(Resource):
    @marshal_with(resource_feilds)
    def get(resource):
        movies = Movie.query.all()
        if not movies:
            abort(404, message = "No movie is there.")
        return movies
        
    @marshal_with(resource_feilds)
    def post(resource):
        args = movie_post_args.parse_args()
        movie = Movie.query.filter_by(movie_name = args['movie_name']).first()
        if movie:
            abort(409, message = "Movie is already exist.")
        input = Movie(movie_name = args["movie_name"], movie_tag = args["movie_tag"], movie_lang = args["movie_lang"], movie_duration = args["movie_duration"])
        db.session.add(input)
        db.session.commit()
        return input,201
        
        
class MovieAPI(Resource):
    @marshal_with(resource_feilds)
    def get(self, movie_id):
        movie = Movie.query.filter_by(movie_id = movie_id).first()
        if not movie:
            abort(404, message="Could not found movie with this movie id")
        return movie
    
    @marshal_with(resource_feilds)
    def put(self,movie_id):
        args = movie_put_args.parse_args()
        movie = Movie.query.filter_by(movie_id = movie_id).first()
        if not movie:
            abort(404, message="Could not found movie with this movie id")
        if args['movie_name']:
            movie.movie_name = args['movie_name']
        if args['movie_tag']:
            movie.movie_tag = args['movie_tag']
        if args['movie_lang']:
            movie.movie_lang = args['movie_lang']
        if args['movie_duration']:
            movie.movie_duration = args['movie_duration'] 
        db.session.commit()
        return movie,200
            
    def delete(self,movie_id):
        movie = Movie.query.filter_by(movie_id = movie_id).first()
        if not movie:
            abort(404, message="Could not found movie with this movie id which you want to delete")
        db.session.delete(movie)
        db.session.commit()
        return jsonify({'status': "Movie deleted", "movie_deleted": movie.movie_name})
    
        