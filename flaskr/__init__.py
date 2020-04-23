import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
import json
from models import setup_db, Player, Match, Settings
from sqlalchemy.orm import relationship
from sqlalchemy import or_

db = SQLAlchemy()
migrate = Migrate()

MATCHES_PER_PAGE = 10

def paginate(page, matches):
    start = (page - 1) * MATCHES_PER_PAGE
    end = start + MATCHES_PER_PAGE
    formated_matches = [match.format() for match in matches]
    return formated_matches[start:end]

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  migrate.init_app(app, db)
  '''
  Set up CORS. Allow '*' for origins.
  '''
  CORS(app, resources={r"/*": {"origins": "*"}})
  '''
  Use the after_request decorator to set Access-Control-Allow
  '''
  @app.after_request
  def after_request(response):
      response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
      response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
      return response
  '''
  Create an endpoint to handle GET requests
  for all available players.
  '''
  @app.route('/players')
  def get_players():
      players = Player.query.all()
      formated_players =  [player.format() for player in players]

      return jsonify({
        'success': True,
        'players': formated_players
      })

  '''
  Create an endpoint to handle GET requests for matches,
  including pagination (every 10 matches).
  This endpoint should return a list of matches,
  number of total matches, current player.
  '''
  @app.route('/matches', methods=['GET'])
  def get_matches():
      page = request.args.get('page', 1, type=int)
      matches = Match.query.all()
      paginated_matches = paginate(page, matches)

      # if there is pagination ot of bounds we abort with 404 Resource Not Found Error
      if len(paginated_matches) == 0:
          abort(404)

      return jsonify({
        'success': True,
        'matches': paginated_matches,
        'total_matches': len(Match.query.all()),
        'current_player': None
        })
  '''
  Endpoint to DELETE match using a match ID.
  '''
  @app.route('/matches/<int:match_id>', methods = ['DELETE'])
  def delete_match(match_id):
      match = Match.query.filter(Match.id==match_id).one_or_none()

      if match == None:
          abort(404)
      else:
          match.delete()
          return jsonify({
          'success': True,
          'match_id': match_id,
          'message': 'Match deleted successfully'
          })

  '''
  @TODO:
  Create an endpoint to POST a new match,
  which will require the player_1_id, player_2_id, player_3_id, player_4_id,
  matchfile, start_time, end_time, type, settings_id, finish

  '''
  @app.route('/matches/create', methods=['POST'])
  def create_match():
      error = False
      try:
          data = json.loads(request.data.decode('utf-8'))
          player_1_id = data['player_1_id']
          player_2_id = data['player_2_id']
          player_3_id = data['player_3_id']
          player_4_id = data['player_4_id']
          matchfile = data['matchfile']
          start_time = data['start_time']
          end_time = data['end_time']
          type = data['type']
          settings_id = data['settings_id']
          finish_state = data['finish_state']

          newMatch = Match(
            player_1_id=player_1_id, player_2_id=player_2_id,
            player_3_id=player_3_id, player_4_id=player_4_id,
            matchfile=matchfile, start_time=start_time,
            end_time=end_time, type=type,
            settings_id=settings_id, finish_state=finish_state
            )
          newMatch.insert()
      except:
          error = True

      if error:
          abort(422)
      else:
          return jsonify({
          'success': True,
          'match': newMatch.format(),
          'total_matches': len(Match.query.all()),
          })

  '''
  Create a POST endpoint to get players based on a search term.
  It should return any players for whom the search term
  is a substring of the name and surename.
  '''
  @app.route('/players/search', methods=['POST'])
  def search_players():
      data = json.loads(request.data.decode('utf-8'))
      search_term = data['searchTerm']
      players = Player.query.filter(
        or_(Player.name.ilike('%' + search_term + '%'),
            Player.surename.ilike('%' + search_term + '%'))
            ).all()

      formated_players = [player.format() for player in players]

      return jsonify({
        'success': True,
        'players': formated_players,
        'total_players': len(players)
      })
  '''
  Create a GET endpoint to get matches based on player.
  '''
  @app.route('/matches/<int:player_id>/matches')
  def get_matches_for_player(player_id):
      matches = Match.query.filter(
        or_(Match.plyers_1_id==player_id,
            Match.plyers_2_id==player_id,
            Match.plyers_3_id==player_id,
            Match.plyers_4_id==player_id
            )).all()

      formated_matches = [match.format() for match in matches]

      return jsonify({
        'success': True,
        'matches': formated_matches,
        'total_matches': len(matches),
        'current_player_id': player_id
      })


  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
    "success": False,
    "error": 400,
    "message": "Bad Request"
    }), 400

  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
    "success": False,
    "error": 404,
    "message": "Resource Not Found"
    }), 404

  @app.errorhandler(405)
  def method_not_allowed(error):
    return jsonify({
    "success": False,
    "error": 405,
    "message": "Method Not Allowed"
    }), 405

  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
    "success": False,
    "error": 422,
    "message": "Unprocessable"
    }), 422

  @app.errorhandler(500)
  def internal_server_error(error):
    return jsonify({
    "success": False,
    "error": 500,
    "message": "Internal Server Error"
    }), 500

  return app
