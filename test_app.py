
import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from psycopg2.extensions import register_adapter, AsIs
from app import create_app
from models import Actors , Movies , setup_db


class CapstoneTestCase(unittest.TestCase):
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "d6cmhnoaos9b2r"
        self.database_path = "postgresql://{}:{}@{}/{}".format('nlvupvrifzdcoz','4ae6bcce2eb595915c6d77d290c4f209fb43aac05dbb2b946c399ec34d0b4be3','localhost:5432', self.database_name)
        self.new_movie = {
            'releaseDate': '14430709',
        }
        self.new_actor = {
            'name': 'shatha',
            'age':'27',
            'gender':'female'
        }
        setup_db(self.app, self.database_path)
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass
    
    def test_404_if_movie_does_not_exist(self):
        response = self.client().delete('/movies/1', headers={
                   "Authorization" : "bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InlHa3lLanVDSlZpcVhXdlp0V1I0SSJ9.eyJpc3MiOiJodHRwczovL2Rldi15NGM4d3N2dC51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTQ3ODAxMTU4MjMzNDcwODM5NTYiLCJhdWQiOlsibGFzdEFwaSIsImh0dHBzOi8vZGV2LXk0Yzh3c3Z0LnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2MzExMTUwNjAsImV4cCI6MTYzMTEyMjI2MCwiYXpwIjoiYjZDQWprakNoN0NoR3ZQdjM3Ull5ZGU0SHJZRThjdEwiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3ItZGV0YWlsIiwiZ2V0Om1vdmllcyIsImdldDptb3ZpZXMtZGV0YWlsIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.rFzC3e9rFe9v1mahfZwFTbz8m1rfaX28EY9tl1pTZF3pA5zq31L9z4FZEIP6gBYJ04_JOzB4lyFEC1gUaJjLYxDgyTA-BBrTmofxqUBEibyVC3o-K8LkZTxw4f4NojZa0xoMI1EWsZ9pw7gNwVg-JkQUZg5_8trTu87lV7OHhsxGkhzlZosx5ueSDj3ahXkL62RCSOpsvpuvdAkUbOmaQkTx4NUFBcV_aIbynaRHpXSn0lLyQZ5etlyXqLu6grdyjG5SPyfQhR14-NJZHmXAtp8ELHYbLgfxFddlJGLNEO2UdBg13cM1m04POCgFNEMJ8RzLg-j43M8913in3hQsug"  
        })
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_404_if_actor_does_not_exist(self):
        response = self.client().delete('/actors/1' , headers={
                   "Authorization" : "bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InlHa3lLanVDSlZpcVhXdlp0V1I0SSJ9.eyJpc3MiOiJodHRwczovL2Rldi15NGM4d3N2dC51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTQ3ODAxMTU4MjMzNDcwODM5NTYiLCJhdWQiOlsibGFzdEFwaSIsImh0dHBzOi8vZGV2LXk0Yzh3c3Z0LnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2MzExMTUwNjAsImV4cCI6MTYzMTEyMjI2MCwiYXpwIjoiYjZDQWprakNoN0NoR3ZQdjM3Ull5ZGU0SHJZRThjdEwiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3ItZGV0YWlsIiwiZ2V0Om1vdmllcyIsImdldDptb3ZpZXMtZGV0YWlsIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.rFzC3e9rFe9v1mahfZwFTbz8m1rfaX28EY9tl1pTZF3pA5zq31L9z4FZEIP6gBYJ04_JOzB4lyFEC1gUaJjLYxDgyTA-BBrTmofxqUBEibyVC3o-K8LkZTxw4f4NojZa0xoMI1EWsZ9pw7gNwVg-JkQUZg5_8trTu87lV7OHhsxGkhzlZosx5ueSDj3ahXkL62RCSOpsvpuvdAkUbOmaQkTx4NUFBcV_aIbynaRHpXSn0lLyQZ5etlyXqLu6grdyjG5SPyfQhR14-NJZHmXAtp8ELHYbLgfxFddlJGLNEO2UdBg13cM1m04POCgFNEMJ8RzLg-j43M8913in3hQsug"  
        })
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_delete_actors(self):
        response = self.client().delete('/actors/1' , headers={
                   "Authorization" : "bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InlHa3lLanVDSlZpcVhXdlp0V1I0SSJ9.eyJpc3MiOiJodHRwczovL2Rldi15NGM4d3N2dC51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTQ3ODAxMTU4MjMzNDcwODM5NTYiLCJhdWQiOlsibGFzdEFwaSIsImh0dHBzOi8vZGV2LXk0Yzh3c3Z0LnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2MzExMTUwNjAsImV4cCI6MTYzMTEyMjI2MCwiYXpwIjoiYjZDQWprakNoN0NoR3ZQdjM3Ull5ZGU0SHJZRThjdEwiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3ItZGV0YWlsIiwiZ2V0Om1vdmllcyIsImdldDptb3ZpZXMtZGV0YWlsIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.rFzC3e9rFe9v1mahfZwFTbz8m1rfaX28EY9tl1pTZF3pA5zq31L9z4FZEIP6gBYJ04_JOzB4lyFEC1gUaJjLYxDgyTA-BBrTmofxqUBEibyVC3o-K8LkZTxw4f4NojZa0xoMI1EWsZ9pw7gNwVg-JkQUZg5_8trTu87lV7OHhsxGkhzlZosx5ueSDj3ahXkL62RCSOpsvpuvdAkUbOmaQkTx4NUFBcV_aIbynaRHpXSn0lLyQZ5etlyXqLu6grdyjG5SPyfQhR14-NJZHmXAtp8ELHYbLgfxFddlJGLNEO2UdBg13cM1m04POCgFNEMJ8RzLg-j43M8913in3hQsug"  
        })
        data = json.loads(response.data)
        actors = Actors.query.filter(Actors.id == 1).one_or_none()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(actors, None)

    def test_delete_movie(self):
        response = self.client().delete('/movies/1' , headers={
                   "Authorization" : "bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InlHa3lLanVDSlZpcVhXdlp0V1I0SSJ9.eyJpc3MiOiJodHRwczovL2Rldi15NGM4d3N2dC51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTQ3ODAxMTU4MjMzNDcwODM5NTYiLCJhdWQiOlsibGFzdEFwaSIsImh0dHBzOi8vZGV2LXk0Yzh3c3Z0LnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2MzExMTUwNjAsImV4cCI6MTYzMTEyMjI2MCwiYXpwIjoiYjZDQWprakNoN0NoR3ZQdjM3Ull5ZGU0SHJZRThjdEwiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3ItZGV0YWlsIiwiZ2V0Om1vdmllcyIsImdldDptb3ZpZXMtZGV0YWlsIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.rFzC3e9rFe9v1mahfZwFTbz8m1rfaX28EY9tl1pTZF3pA5zq31L9z4FZEIP6gBYJ04_JOzB4lyFEC1gUaJjLYxDgyTA-BBrTmofxqUBEibyVC3o-K8LkZTxw4f4NojZa0xoMI1EWsZ9pw7gNwVg-JkQUZg5_8trTu87lV7OHhsxGkhzlZosx5ueSDj3ahXkL62RCSOpsvpuvdAkUbOmaQkTx4NUFBcV_aIbynaRHpXSn0lLyQZ5etlyXqLu6grdyjG5SPyfQhR14-NJZHmXAtp8ELHYbLgfxFddlJGLNEO2UdBg13cM1m04POCgFNEMJ8RzLg-j43M8913in3hQsug"  
        })
        data = json.loads(response.data)
        movies = Movies.query.filter(Movies.id == 1).one_or_none()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(movies, None)

    def test_create_new_actor(self):
        actorBefore = len(Actors.query.all())
        response = self.client().post('/actors', json=self.new_actor , headers={
                   "Authorization" : "bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InlHa3lLanVDSlZpcVhXdlp0V1I0SSJ9.eyJpc3MiOiJodHRwczovL2Rldi15NGM4d3N2dC51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTQ3ODAxMTU4MjMzNDcwODM5NTYiLCJhdWQiOlsibGFzdEFwaSIsImh0dHBzOi8vZGV2LXk0Yzh3c3Z0LnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2MzExMTUwNjAsImV4cCI6MTYzMTEyMjI2MCwiYXpwIjoiYjZDQWprakNoN0NoR3ZQdjM3Ull5ZGU0SHJZRThjdEwiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3ItZGV0YWlsIiwiZ2V0Om1vdmllcyIsImdldDptb3ZpZXMtZGV0YWlsIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.rFzC3e9rFe9v1mahfZwFTbz8m1rfaX28EY9tl1pTZF3pA5zq31L9z4FZEIP6gBYJ04_JOzB4lyFEC1gUaJjLYxDgyTA-BBrTmofxqUBEibyVC3o-K8LkZTxw4f4NojZa0xoMI1EWsZ9pw7gNwVg-JkQUZg5_8trTu87lV7OHhsxGkhzlZosx5ueSDj3ahXkL62RCSOpsvpuvdAkUbOmaQkTx4NUFBcV_aIbynaRHpXSn0lLyQZ5etlyXqLu6grdyjG5SPyfQhR14-NJZHmXAtp8ELHYbLgfxFddlJGLNEO2UdBg13cM1m04POCgFNEMJ8RzLg-j43M8913in3hQsug"  
        })
        data = json.loads(response.data)
        actorAfter = len(Actors.query.all())
        actor = Actors.query.filter_by(id=data['created']).all()
        self.assertIsNotNone(actor)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(actorAfter, actorBefore + 1)

    def test_create_new_movie(self):
        movieBefore = len(Movies.query.all())
        response = self.client().post('/movies', json=self.new_movie , headers={
                   "Authorization" : "bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InlHa3lLanVDSlZpcVhXdlp0V1I0SSJ9.eyJpc3MiOiJodHRwczovL2Rldi15NGM4d3N2dC51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTQ3ODAxMTU4MjMzNDcwODM5NTYiLCJhdWQiOlsibGFzdEFwaSIsImh0dHBzOi8vZGV2LXk0Yzh3c3Z0LnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2MzExMTUwNjAsImV4cCI6MTYzMTEyMjI2MCwiYXpwIjoiYjZDQWprakNoN0NoR3ZQdjM3Ull5ZGU0SHJZRThjdEwiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3ItZGV0YWlsIiwiZ2V0Om1vdmllcyIsImdldDptb3ZpZXMtZGV0YWlsIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.rFzC3e9rFe9v1mahfZwFTbz8m1rfaX28EY9tl1pTZF3pA5zq31L9z4FZEIP6gBYJ04_JOzB4lyFEC1gUaJjLYxDgyTA-BBrTmofxqUBEibyVC3o-K8LkZTxw4f4NojZa0xoMI1EWsZ9pw7gNwVg-JkQUZg5_8trTu87lV7OHhsxGkhzlZosx5ueSDj3ahXkL62RCSOpsvpuvdAkUbOmaQkTx4NUFBcV_aIbynaRHpXSn0lLyQZ5etlyXqLu6grdyjG5SPyfQhR14-NJZHmXAtp8ELHYbLgfxFddlJGLNEO2UdBg13cM1m04POCgFNEMJ8RzLg-j43M8913in3hQsug"  
        })
        data = json.loads(response.data)
        movieAfter = len(Movies.query.all())
        movie = Movies.query.filter_by(id=data['created']).all()
        self.assertIsNotNone(movie)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(movieAfter, movieBefore + 1)

    def test_400_if_movie_creation_fails(self):
        response = self.client().post('/movies', json={} , headers={
                   "Authorization" : "bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InlHa3lLanVDSlZpcVhXdlp0V1I0SSJ9.eyJpc3MiOiJodHRwczovL2Rldi15NGM4d3N2dC51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTQ3ODAxMTU4MjMzNDcwODM5NTYiLCJhdWQiOlsibGFzdEFwaSIsImh0dHBzOi8vZGV2LXk0Yzh3c3Z0LnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2MzExMTUwNjAsImV4cCI6MTYzMTEyMjI2MCwiYXpwIjoiYjZDQWprakNoN0NoR3ZQdjM3Ull5ZGU0SHJZRThjdEwiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3ItZGV0YWlsIiwiZ2V0Om1vdmllcyIsImdldDptb3ZpZXMtZGV0YWlsIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.rFzC3e9rFe9v1mahfZwFTbz8m1rfaX28EY9tl1pTZF3pA5zq31L9z4FZEIP6gBYJ04_JOzB4lyFEC1gUaJjLYxDgyTA-BBrTmofxqUBEibyVC3o-K8LkZTxw4f4NojZa0xoMI1EWsZ9pw7gNwVg-JkQUZg5_8trTu87lV7OHhsxGkhzlZosx5ueSDj3ahXkL62RCSOpsvpuvdAkUbOmaQkTx4NUFBcV_aIbynaRHpXSn0lLyQZ5etlyXqLu6grdyjG5SPyfQhR14-NJZHmXAtp8ELHYbLgfxFddlJGLNEO2UdBg13cM1m04POCgFNEMJ8RzLg-j43M8913in3hQsug"  
        })
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Bad Request')
    
    def test_400_if_actor_creation_fails(self):
        response = self.client().post('/actors', json={} , headers={
                   "Authorization" : "bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InlHa3lLanVDSlZpcVhXdlp0V1I0SSJ9.eyJpc3MiOiJodHRwczovL2Rldi15NGM4d3N2dC51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTQ3ODAxMTU4MjMzNDcwODM5NTYiLCJhdWQiOlsibGFzdEFwaSIsImh0dHBzOi8vZGV2LXk0Yzh3c3Z0LnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2MzExMTUwNjAsImV4cCI6MTYzMTEyMjI2MCwiYXpwIjoiYjZDQWprakNoN0NoR3ZQdjM3Ull5ZGU0SHJZRThjdEwiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3ItZGV0YWlsIiwiZ2V0Om1vdmllcyIsImdldDptb3ZpZXMtZGV0YWlsIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.rFzC3e9rFe9v1mahfZwFTbz8m1rfaX28EY9tl1pTZF3pA5zq31L9z4FZEIP6gBYJ04_JOzB4lyFEC1gUaJjLYxDgyTA-BBrTmofxqUBEibyVC3o-K8LkZTxw4f4NojZa0xoMI1EWsZ9pw7gNwVg-JkQUZg5_8trTu87lV7OHhsxGkhzlZosx5ueSDj3ahXkL62RCSOpsvpuvdAkUbOmaQkTx4NUFBcV_aIbynaRHpXSn0lLyQZ5etlyXqLu6grdyjG5SPyfQhR14-NJZHmXAtp8ELHYbLgfxFddlJGLNEO2UdBg13cM1m04POCgFNEMJ8RzLg-j43M8913in3hQsug"  
        })
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Bad Request')


    def test_get_actor(self):
        res = self.client().get('/Actor' , headers={
                   "Authorization" : "bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InlHa3lLanVDSlZpcVhXdlp0V1I0SSJ9.eyJpc3MiOiJodHRwczovL2Rldi15NGM4d3N2dC51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTQ3ODAxMTU4MjMzNDcwODM5NTYiLCJhdWQiOlsibGFzdEFwaSIsImh0dHBzOi8vZGV2LXk0Yzh3c3Z0LnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2MzExMTUwNjAsImV4cCI6MTYzMTEyMjI2MCwiYXpwIjoiYjZDQWprakNoN0NoR3ZQdjM3Ull5ZGU0SHJZRThjdEwiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3ItZGV0YWlsIiwiZ2V0Om1vdmllcyIsImdldDptb3ZpZXMtZGV0YWlsIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.rFzC3e9rFe9v1mahfZwFTbz8m1rfaX28EY9tl1pTZF3pA5zq31L9z4FZEIP6gBYJ04_JOzB4lyFEC1gUaJjLYxDgyTA-BBrTmofxqUBEibyVC3o-K8LkZTxw4f4NojZa0xoMI1EWsZ9pw7gNwVg-JkQUZg5_8trTu87lV7OHhsxGkhzlZosx5ueSDj3ahXkL62RCSOpsvpuvdAkUbOmaQkTx4NUFBcV_aIbynaRHpXSn0lLyQZ5etlyXqLu6grdyjG5SPyfQhR14-NJZHmXAtp8ELHYbLgfxFddlJGLNEO2UdBg13cM1m04POCgFNEMJ8RzLg-j43M8913in3hQsug"  
        })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    

    def test_get_movie(self):
        res = self.client().get('/Movies' , headers={
                   "Authorization" : "bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InlHa3lLanVDSlZpcVhXdlp0V1I0SSJ9.eyJpc3MiOiJodHRwczovL2Rldi15NGM4d3N2dC51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTQ3ODAxMTU4MjMzNDcwODM5NTYiLCJhdWQiOlsibGFzdEFwaSIsImh0dHBzOi8vZGV2LXk0Yzh3c3Z0LnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2MzExMTUwNjAsImV4cCI6MTYzMTEyMjI2MCwiYXpwIjoiYjZDQWprakNoN0NoR3ZQdjM3Ull5ZGU0SHJZRThjdEwiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3ItZGV0YWlsIiwiZ2V0Om1vdmllcyIsImdldDptb3ZpZXMtZGV0YWlsIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.rFzC3e9rFe9v1mahfZwFTbz8m1rfaX28EY9tl1pTZF3pA5zq31L9z4FZEIP6gBYJ04_JOzB4lyFEC1gUaJjLYxDgyTA-BBrTmofxqUBEibyVC3o-K8LkZTxw4f4NojZa0xoMI1EWsZ9pw7gNwVg-JkQUZg5_8trTu87lV7OHhsxGkhzlZosx5ueSDj3ahXkL62RCSOpsvpuvdAkUbOmaQkTx4NUFBcV_aIbynaRHpXSn0lLyQZ5etlyXqLu6grdyjG5SPyfQhR14-NJZHmXAtp8ELHYbLgfxFddlJGLNEO2UdBg13cM1m04POCgFNEMJ8RzLg-j43M8913in3hQsug"  
        })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


        
if __name__ == "__main__":
    unittest.main()