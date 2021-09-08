from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Integer
import json
from collections import namedtuple

database_name = "postgres"
database_path = "postgresql://{}:{}@{}/{}".format('postgres','Shosho11','127.0.0.1:5432', database_name)

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

class Movies(db.Model):
    __tablename__ = 'Movie'
    id = db.Column(Integer,primary_key=True,nullable=False, unique=True, autoincrement=True)
    releaseDate = db.Column(db.String) 
 
    def format(self):
      return {
          'id': self.id,
          'releaseDate': self.releaseDate,
    }  
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def long(self):
       return {
           'id': self.id,
           'releaseDate': json.loads(self.releaseDate)
        }
    def update(self):
        db.session.commit()


class Actors(db.Model):
    __tablename__ = 'Actor'
    id = db.Column(db.Integer,primary_key=True,nullable=False, unique=True, autoincrement=True)
    name = db.Column(db.String)
    age  = db.Column(db.String)
    gender = db.Column(db.String(120))

    def format(self):
      return {
          'id': self.id,
          'name': self.name,
          'age': self.age,
          'gender': self.gender,

    }  
    def long(self):
       return {
           'id': self.id,
           'name': json.loads(self.name),
           'age': json.loads(self.age),
           'gender': json.loads(self.gender),
        }
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def insert(self):
        db.session.add(self)
        db.session.commit()

