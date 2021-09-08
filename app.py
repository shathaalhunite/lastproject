import os
import re
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from models import Movies,Actors,setup_db
from auth.app import AuthError, requires_auth
import json
from logging import DEBUG, Formatter, FileHandler
import logging


# setup_db(app)
# db.create_all()
def create_app(test_config=None):
    
    app = Flask(__name__, instance_relative_config=True)
    db = SQLAlchemy(app)
    migrate = Migrate(app, db, compare_type=True)
    manager = Manager(app)  
    manager.add_command('db', MigrateCommand)
    app.config.from_object('config')  
    setup_db(app)
    CORS(app, resources={'/': {'origins': '*'}})

    
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods','GET,PUT,POST,DELETE,OPTIONS')
        return response

    @app.route('/Movies', methods=['GET'])
    def getMovies():
        movies = Movies.query.all()
        formatted_movies = [movie.format() for movie in movies]
        if (len(formatted_movies) == 0):
                abort(404)

        return jsonify({
            'success': True,
            'movies': formatted_movies
        }), 200

    @app.route('/Actor', methods=['GET'])
    def getActors():
        actor = Actors.query.all()
        formatted_actor = [actor.format() for actor in actor]
        if (len(formatted_actor) == 0):
            abort(404)

        return jsonify({
            'success': True,
            'actors': formatted_actor
       }), 200

    @app.route('/movies-detail', methods=['GET'])
    @requires_auth('get:movies-detail')
    def getMoviesdetails(payload):
        movies = Movies.query.all()
        formatted_movies = [movie.format() for movie in movies]
        if (len(formatted_movies) == 0):
            abort(404)
        return jsonify({
            'success': True,
            'movies': formatted_movies
        }), 200

    @app.route('/actor-detail', methods=['GET'])
    @requires_auth('get:actor-detail')
    def getActorsdetails(payload):
        actors = Actors.query.all()
        formatted_actor = [actor.format() for actor in actors]
        if (len(formatted_actor) == 0):
            abort(404)
        return jsonify({
            'success': True,
            'movies': formatted_actor
        }), 200

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def postMovie(payload):
        req = request.get_json()
        try:
            req = req['releaseDate']
            if isinstance(req, dict):
                req = [req]

            movie = Movies()
            movie.releaseDate = json.dumps(req)
            movie.insert()
        except BaseException:
            abort(400)
        return jsonify({
            'success': True,
            'created': movie.id,
            'movies': [movie.long()]})

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def postActor(payload):
        body = request.get_json()
        try:
             reqName = body['name'],
             reqAge = body['age'],
             reqGender = body['gender']
    
             actor = Actors()
             actor.name = json.dumps(reqName)
             actor.age = json.dumps(reqAge)
             actor.gender = json.dumps(reqGender)
             actor.insert()
        except BaseException:
            abort(400)
        return jsonify({
            'success': True,
            'created': actor.id,
            'total_questions': len(Actors.query.all())
               })


    @app.route('/movies/<int:id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def PATCH_movies(payload, id):
        req = request.get_json()
        movie = Movies.query.filter(Movies.id == id).one_or_none()
        id=req['id']
        releaseDate = req['releaseDate']
        if id:
            movie.id = id

        if releaseDate:
            movie.releaseDate = json.dumps(req['releaseDate'])

        movie.update()
        return jsonify({'success': True, 'movies': [movie.long()]}), 200

    @app.route('/actors/<int:id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def PATCH_actor(payload, id):
        req = request.get_json()
        actor = Actors.query.filter(Actors.id == id).one_or_none()
        id=req['id']
        name = req['name']
        age = req['age']
        gender = req['gender']
        if id:
            actor.id = id

        if name:
            actor.name = json.dumps(req['name'])
        if age:
            actor.age = json.dumps(req['age'])
        if gender:
            actor.gender = json.dumps(req['gender'])

        actor.update()
        return jsonify({'success': True, 'actors': [actor.long()]}), 200


    @app.route('/movies/<int:id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def deleteMovie(payload, id):
        movie = Movies.query.filter(Movies.id == id).one_or_none()
        print(movie)
        if not movie:
            abort(404)
        try:
            movie.delete()
        except BaseException:
            abort(400)

        return jsonify({'success': True, 'delete': id}), 200

    @app.route('/actors/<int:id>', methods=['DELETE'])
    @requires_auth('delete:actors')    
    def deleteActor(payload, id):
        actor = Actors.query.filter(Actors.id == id).one_or_none()
        if not actor:
            abort(404)
        try:
            actor.delete()
        except BaseException:
            abort(400)

        return jsonify({'success': True, 'delete': id}), 200

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422



    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404


    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": 'Internal Server Error'
        }), 500


    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": 'Bad Request'
        }), 400

    return app