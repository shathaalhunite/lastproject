import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

database_name = "postgres"
database_path = "postgres://{}:{}@{}/{}".format('postgres','Shosho11','localhost:5432', database_name)

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

'''
Movies

'''
class Movies(db.Model):  
     __tablename__ = 'questions'
     id = Column(Integer, primary_key=True)
     title = Column(String)
     relase_date = Column(String)


def __init__(self, question, answer):
    self.title = question
    self.relase_date = answer
   

def insert(self):
    db.session.add(self)
    db.session.commit()
  
def update(self):
    db.session.commit()

def delete(self):
    db.session.delete(self)
    db.session.commit()

def format(self):
    return {
      'id': self.id,
      'title': self.title,
      'relasedate': self.relase_date,

    }

'''
Actors

'''
class Actors(db.Model):  
     __tablename__ = 'categories'

     id = Column(Integer, primary_key=True)
     name = Column(String)
     age = Column(Integer)
     gender = Column(String)

def __init__(self, name ,age , gender):
    self.name = name
    self.age = age
    self.gender = gender

def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'age': self.age,
      'gender': self.gender,
    }