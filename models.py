import os
from sqlalchemy import Column, String, Integer, create_engine, DateTime, ForeignKey, Boolean
from flask_sqlalchemy import SQLAlchemy
import json

DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD', 'postgres')

database_name = "orange"
database_path = "postgres://{}:{}@{}/{}".format('postgres', DATABASE_PASSWORD, 'localhost:5432', database_name)

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
Players

'''
class Player(db.Model):
  __tablename__ = 'players'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  surname = Column(String)
  nationality = Column(String)
  year = Column(Integer)
  gender = Column(String)
  weight = Column(Integer)
  height = Column(Integer)

  def __init__(self, name, surname, nationality, year, gender, weight, height):
    self.name = name
    self.surname = surname
    self.nationality = nationality
    self.year = year
    self.gender = gender
    self.weight = weight
    self.height = height

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
      'name': self.name,
      'surname': self.surname,
      'nationality': self.nationality,
      'year': self.year,
      'gender': self.gender,
      'weight': self.weight,
      'height': self.height
    }

'''
Matches

'''
class Match(db.Model):
  __tablename__ = 'matches'

  id = Column(Integer, primary_key=True)
  player_1_id = Column('player_1_id', Integer, ForeignKey('players.id'), nullable = False)
  player_2_id = Column('player_2_id', Integer, ForeignKey('players.id'), nullable = False)
  player_3_id = Column('player_3_id', Integer, ForeignKey('players.id'), nullable = True)
  player_4_id = Column('player_4_id', Integer, ForeignKey('players.id'), nullable = True)
  matchfile = Column(String) # this is array of all points played converted to JSON object and saved as String
  start_time = Column('start_time', db.DateTime, nullable = False)
  end_time = Column('end_time', db.DateTime, nullable = True)
  type = Column(Integer) # singles = 1, doubles= 2, mixed = 3
  settings_id = Column('settings_id', Integer, ForeignKey('settings.id'), nullable = False)
  finish_state = Column(Integer) #not finished = 0, finished = 1,  urrendered = 2

  def __init__(self,
    player_1_id, player_2_id, player_3_id, player_4_id,
    matchfile, start_time, end_time, type, settings_id, finish):
    self.player_1_id = player_1_id
    self.player_2_id = player_2_id
    self.player_3_id = player_3_id
    self.player_4_id = player_4_id
    self.matchfile = matchfile
    self.start_time = start_time
    self.end_time = end_time
    self.type = type
    self.settings = settings_id
    self.finish = finish

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
      'player_1_id': self.player_1_id,
      'player_2_id': self.player_1_id,
      'player_3_id': self.player_1_id,
      'player_4_id': self.player_1_id,
      'matchfile': self.matchfile,
      'start_time': self.start_time,
      'end_time': self.end_time,
      'type': self.type,
      'settings': self.settings,
      'finish': self.finish,
    }

'''
Settings

'''
class Settings(db.Model):
  __tablename__ = 'settings'

  id = Column(Integer, primary_key=True)
  number_of_gamest_to_win = Column('number_of_gamest_to_win', Integer, nullable = False)
  number_of_sets_to_win = Column('number_of_sets_to_win', Integer, nullable = False)
  advantage = Column('advantage', Boolean,  nullable = False)
  tiebreak = Column('tiebreak', Boolean,  nullable = False)
  points_in_tiebreak = Column('points_in_tiebreak', Integer, nullable = False)
  play_last_set_as_tiebreak = Column('play_last_set_as_tiebreak', Boolean, nullable = False)
  serve_locked = Column('serve_locked', Boolean,  nullable = False)
  tiebreak_difference = Column('tiebreak_difference', Integer, nullable = False)


  def __init__(self,
    number_of_gamest_to_win, number_of_sets_to_win, advantage, tiebreak, points_in_tiebreak,
    play_last_set_as_tiebreak, serve_locked, tiebreak_difference):
    self.number_of_gamest_to_win = number_of_gamest_to_win
    self.number_of_sets_to_win = number_of_sets_to_win
    self.advantage = advantage
    self.tiebreak = tiebreak
    self.points_in_tiebreak = points_in_tiebreak
    self.play_last_set_as_tiebreak = play_last_set_as_tiebreak
    self.serve_locked = serve_locked
    self.tiebreak_difference = tiebreak_difference

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
      'number_of_gamest_to_win': self.number_of_gamest_to_win,
      'number_of_sets_to_win': self.number_of_sets_to_win,
      'advantage': self.advantage,
      'tiebreak': self.tiebreak,
      'points_in_tiebreak': self.points_in_tiebreak,
      'play_last_set_as_tiebreak': self.play_last_set_as_tiebreak,
      'serve_locked': self.serve_locked,
      'tiebreak_difference': self.tiebreak_difference
    }
