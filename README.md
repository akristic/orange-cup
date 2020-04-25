# Orange Cup
 Udacity Capstone Project for Full stack ND
 -----

 ### Introduction

 Orange cup is tennis web app for keeping score of tennis matches. It is a backend API created for Udacity Capstone Project for Full stack ND. This is backend for site that allows user to login, create players and matches and share them with the world. My motivation for this project is that after completing this Nanodegree I will continue to work on this project and make professional web site that will be connected with android app Orange Cup.
 You can find sample of this project on heroku: https://orangecup.herokuapp.com/


#### Virtual Enviornment

It is recommended working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/` root directory and running:

```bash
pip install -r requirements.txt
```
##Create database
 - create database in psql with name "orange"

## Running the server
From within the root directory first ensure you are working using your created virtual environment.
To run the server, execute:

```bash
export FLASK_APP=app
export FLASK_ENV=development
flask run
```
Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.


# For testing endpoints in postman you will need VALID token.
This token will be provided to Udacity in submission. (2 Tokens. One for User and one for Admin)

To get your own tokens you will need to make your own account on Auth0. And in auth/auth.py file you will need to change
AUTH0_DOMAIN = 'orangecup.auth0.com'
API_AUDIENCE = 'orange'
to values from your account.
There are 2 roles setup in Auth0:
 - User with permissions:
    - read:matches
    - read:players
    - read:settings
    - write:matches
    - write:players
read:players and read:matches is actually not needed because currently everyone can read players and matches

  - Admin with permissions:
    - read:matches
    - read:players
    - read:settings
    - write:matches
    - write:players
    - write:settings
    - delete:matches
    - delete:players
    - delete:settings

To login create link like this:
https://orangecup.auth0.com/authorize?audience=orange&response_type=token&client_id=fXWf5reNlyMSgq4TjxQ23vvhtYFrZzsV&redirect_uri=https://localhost:8080/login-results
but change values with ones from your account

After successfully login you will be redirected to login-result page but because there is no frontend you will land on This site can’t be reached page. Just copy token from url created in your browser. It will look something like this:
```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ikxza1ZQMGtWOXpMSGhUU1pzSDRXeCJ9.eyJpc3MiOiJodHRwczovL29yYW5nZWN1cC5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTE3OTMyNzA5MTk5MDIxODI0MzciLCJhdWQiOlsib3JhbmdlIiwiaHR0cHM6Ly9vcmFuZ2VjdXAuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTU4NzcwNDk4OSwiZXhwIjoxNTg3NzEyMTg5LCJhenAiOiJmWFdmNXJlTmx5TVNncTRUanhRMjN2dmh0WUZyWnpzViIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6bWF0Y2hlcyIsImRlbGV0ZTpwbGF5ZXJzIiwiZGVsZXRlOnNldHRpbmdzIiwicmVhZDptYXRjaGVzIiwicmVhZDpwbGF5ZXJzIiwicmVhZDpzZXR0aW5ncyIsIndyaXRlOm1hdGNoZXMiLCJ3cml0ZTpwbGF5ZXJzIiwid3JpdGU6c2V0dGluZ3MiXX0.jmce8wwNdsNo3xWSdhvqHEyKsbWYxNpMzzCbCswnhawRxDhEMHk-TifslD3jMwcs77X_89isVsed4upT2yQtSu_xpK2GskInTdtxffycoctD-d9AFpu67NphPtZDUZjw_ay0hhYaLrmvLBCelTkS6u4P2TuxpeL3rI5nb_zUhFaqwsB8a4kkUvAk0UOhX1jxLCXxyifjZH4KtQ7MtkFpG3hZ842QYlo12wv5N3frfenFlVHNQMGC2Y2Jr1dAqD_RUQDYjE0babTbukSxjRoYXLmx2okrU3K-o--EoarztWOgFjSSq_b6LkrZHiSBnoAkx7YNU3nC9FIRpbifCDx6cA
```
# Testing with Postman
Import collection in postman from file: orange-cup-endpoint-test-collection.postman_collection
In postman under Authorization tab select Type of authorization to OAuth 2.0. Use newly created token and paste it in Access Token box.
Important: Run all POST test under admin folder to populate database. Do this 3 or more times to have at least 3 rows in database. First create 3 players, than 3 settings and than 3 matches. Order is important because you can't create matches without valid player and settings primary keys.

# Endpoints
- GET '/'
- GET '/players'
- POST '/players/create'
- POST '/players/search'
- PATCH '/players/<int:player_id>'
- DELETE '/players/<int:player_id>'

- GET ''/settings'
- POST '/settings/create'
- DELETE '/settings/<int:settings_id>'

- GET '/matches'
- GET '/players/<int:player_id>/matches'
- POST '/matches/create'
- DELETE '/matches/<int:match_id>'

## GET '/'
- Fetches information that are used as index page
- Request Arguments: None
- Response:  JSON object with basic information

Response Example:
```
{
  "git_url": "https://github.com/akristic/orange-cup",
  "public endpoints": [
    "/players",
    "/matches"
  ],
  "success": true,
  "welcome_message": "Hooray, Welocome to Orange Cup",
  "what_next": "Go to Github and read Readme.txt file or try some public endpoints"
}
```
## GET '/players'
- Fetches a list of players
- Request Arguments: None
- Response:  JSON object that contains:
  - success state (True) - means everything is ok
  - players list: each player has all information about player
Response Example:
```
{
  "players": [
    {
      "gender": "male",
      "height": 180,
      "id": 3,
      "name": "FirstName",
      "nationality": "DE",
      "surname": "Surname",
      "weight": 80,
      "year": 1981
    },
    {
      "gender": "male",
      "height": 180,
      "id": 4,
      "name": "Ante",
      "nationality": "HR",
      "surname": "Kristic",
      "weight": 75,
      "year": 1981
    }
  ],
  "success": true
}
```

## POST '/players/create''
- Creates new player and save it in database
- Request Arguments: body data with key value pairs
Body Example:
```
{
"name":"Ante",
"surname":"Kristic",
"nationality":"HR",
"year":1981,
"gender":"male",
"weight":75,
"height":180
}
```
- Response:  JSON object that contains:
  - success state (True) - means everything is ok
  - players: player with all information that is just created
  - total players: number of total players in database
Response Example:
```
{
    "player": {
        "gender": "male",
        "height": 180,
        "id": 5,
        "name": "FirstName",
        "nationality": "DE",
        "surname": "Surname",
        "weight": 80,
        "year": 1981
    },
    "success": true,
    "total_players": 5
}
```
## POST '/players/search'
- Search players with given search keyword in player name and surname
- Request Arguments: body data with key value pairs
Body Example:
```
{
  "search_term":"kri"
}
```
- Response:  JSON object that contains:
  - success state (True) - means everything is ok
  - players: list of players with all information
  - total players: number of players found in database
Response Example:
```
{
    "players": [
        {
            "gender": "male",
            "height": 180,
            "id": 4,
            "name": "Ante",
            "nationality": "HR",
            "surname": "Kristic",
            "weight": 75,
            "year": 1981
        },
        {
            "gender": "male",
            "height": 180,
            "id": 2,
            "name": "Ante",
            "nationality": "HR",
            "surname": "Kristic",
            "weight": 74,
            "year": 1981
        }
    ],
    "success": true,
    "total_players_found": 2
}
```

## PATCH '/players/<int:player_id>'
- Updates players with given player_id
- Request Arguments:
  - Id of player we want to update,
    example: '/players/6' will update player with id=6
  - body data with key value pairs, you don't have to
    include all data, just the one you need to update
Body Example:
```
{
"name": "John",
"gender": "male",
"height": 180,
"nationality": "DE",
"surname": "Smith",
"weight": 75,
"year": 1988
}
```
- Response:  JSON object that contains:
  - success state (True) - means everything is ok
  - player id: Id of player that is just updated
  - message: short message that describes what just happened
Response Example:
```
{
    "message": "Player updated successfully",
    "player_id": 2,
    "success": true
}
```
## DELETE '/players/<int:player_id>'
 - Deleting player with given player id
 - Request Arguments: Id of player we want to delete,
   example: '/players/42' will delete player with id=42
 - Response:  JSON object that contains:
     - success state (True) - means everything is ok
     - player id: Id of player that is just deleted
     - message: short message that describes what just happened
Response Example:
```
{
    "message": "Player deleted successfully",
    "player_id": 3,
    "success": true
}
```

## GET ''/settings'
 - Fetches list of settings
 - Request Arguments: None,
 - Response:  JSON object that contains:
     - success state (True) - means everything is ok
     - settings: list of matches settings need for every match we play

Response Example:
```
{
    "settings": [
        {
            "advantage": true,
            "id": 1,
            "number_of_games_to_win": 6,
            "number_of_sets_to_win": 2,
            "play_last_set_as_tiebreak": true,
            "points_in_tiebreak": 6,
            "serve_locked": true,
            "tiebreak": true,
            "tiebreak_difference": 1
        },
        {
            "advantage": true,
            "id": 2,
            "number_of_games_to_win": 6,
            "number_of_sets_to_win": 3,
            "play_last_set_as_tiebreak": false,
            "points_in_tiebreak": 6,
            "serve_locked": true,
            "tiebreak": true,
            "tiebreak_difference": 2
        }
    ],
    "success": true
}
```

## POST '/settings/create'
 - Create new settings and save it in database
 - Request Arguments:  body data with key value pairs, all data must be included
Body Example:
```
{
"number_of_games_to_win":6,
"number_of_sets_to_win":3,
"advantage":true,
"tiebreak":true,
"points_in_tiebreak":6,
"play_last_set_as_tiebreak":false,
"serve_locked":true,
"tiebreak_difference":2
}
```

 - Response:  JSON object that contains:
     - success state (True) - means everything is ok
     - settings: all information about settings that we just created
     - total settings: number of settings in database
Response Example:
```
{
    "settings": {
        "advantage": true,
        "id": 4,
        "number_of_games_to_win": 6,
        "number_of_sets_to_win": 3,
        "play_last_set_as_tiebreak": false,
        "points_in_tiebreak": 6,
        "serve_locked": true,
        "tiebreak": true,
        "tiebreak_difference": 2
    },
    "success": true,
    "total_settings": 4
}
```

## DELETE '/settings/<int:settings_id>'
 - Deleting settings with given settings id
 - Request Arguments: Id of settings we want to delete,
   example: '/settings/3' will delete settings with id=3
 - Response:  JSON object that contains:
     - success state (True) - means everything is ok
     - settings id: Id of settings that is just deleted
     - message: short message that describes what just happened
Response Example:
```
{
    "message": "Settings deleted successfully",
    "settings_id": 1,
    "success": true
}
```

## GET '/matches'
 - Fetches a list of 10 matches per page
 - Request Arguments: 'page' (type: Integer, default is 1) - not required
   example: '/matches?page=3' will return matches from 20 to 29 included
 - Response:  JSON object that contains:
     - success state (True) - means everything is ok
     - current player: This part is for new feature, nothing to do with this right now
     - matches: list of max 10 paginated matches
     - total matches: number of all matches in database
Response Example:
```
{
    "current_player": null,
    "matches": [
        {
            "end_time": null,
            "finish_state": 0,
            "id": 2,
            "matchfile": "fake json string for testing",
            "player_1_id": 1,
            "player_2_id": 2,
            "player_3_id": null,
            "player_4_id": null,
            "settings_id": 2,
            "start_time": "Wed, 22 Jun 2016 19:10:25 GMT",
            "type": 1
        },
        {
            "end_time": null,
            "finish_state": 0,
            "id": 3,
            "matchfile": "fake json string for testing",
            "player_1_id": 1,
            "player_2_id": 2,
            "player_3_id": null,
            "player_4_id": null,
            "settings_id": 2,
            "start_time": "Wed, 22 Jun 2016 19:10:25 GMT",
            "type": 1
        },
        {
            "end_time": null,
            "finish_state": 0,
            "id": 4,
            "matchfile": "fake json string for testing",
            "player_1_id": 1,
            "player_2_id": 2,
            "player_3_id": null,
            "player_4_id": null,
            "settings_id": 2,
            "start_time": "Wed, 22 Jun 2016 19:10:25 GMT",
            "type": 1
        }
    ],
    "success": true,
    "total_matches": 3
}
```
## GET '/players/<int:player_id>/matches'
 - Fetches matches with given player id
 - Request Arguments: Id of player we want to fetch,
   example: '/player/3/matches' will fetch all matches that player with id 3 has played
 - Response:  JSON object that contains:
     - success state (True) - means everything is ok
     - player id: Id of player that played in all fetched matches
     - matches:  list of matches that player with player_id has played
     - total matches: number of matches found with given criteria
Response Example:
```
{
    "current_player_id": 2,
    "matches": [
        {
            "end_time": null,
            "finish_state": 0,
            "id": 2,
            "matchfile": "fake json string for testing",
            "player_1_id": 1,
            "player_2_id": 2,
            "player_3_id": null,
            "player_4_id": null,
            "settings_id": 2,
            "start_time": "Wed, 22 Jun 2016 19:10:25 GMT",
            "type": 1
        },
        {
            "end_time": null,
            "finish_state": 0,
            "id": 3,
            "matchfile": "fake json string for testing",
            "player_1_id": 1,
            "player_2_id": 2,
            "player_3_id": null,
            "player_4_id": null,
            "settings_id": 2,
            "start_time": "Wed, 22 Jun 2016 19:10:25 GMT",
            "type": 1
        },
        {
            "end_time": null,
            "finish_state": 0,
            "id": 4,
            "matchfile": "fake json string for testing",
            "player_1_id": 1,
            "player_2_id": 2,
            "player_3_id": null,
            "player_4_id": null,
            "settings_id": 2,
            "start_time": "Wed, 22 Jun 2016 19:10:25 GMT",
            "type": 1
        }
    ],
    "success": true,
    "total_matches": 3
}
```
## POST '/matches/create'
 - Creating new match and save it in database
 - Request Arguments: body data with key value pairs, all data must be included,

Body Example:
```
{
"player_1_id":2,
"player_2_id":3,
"player_3_id":null,
"player_4_id":null,
"matchfile":"fake json string for testing",
"start_time":"2016-06-22 19:10:25-07",
"end_time":null,
"type":1,
"settings_id":2,
"finish_state":0
}
```
 - Response:  JSON object that contains:
     - success state (True) - means everything is ok
     - match: all information about match we just created
     - total matches: number of all matches in database
Response Example:
```
{
    "match": {
        "end_time": null,
        "finish_state": 0,
        "id": 5,
        "matchfile": "fake json string for testing",
        "player_1_id": 1,
        "player_2_id": 2,
        "player_3_id": null,
        "player_4_id": null,
        "settings_id": 2,
        "start_time": "Wed, 22 Jun 2016 19:10:25 GMT",
        "type": 1
    },
    "success": true,
    "total_matches": 4
}
```
## DELETE '/matches/<int:match_id>'
 - Deleting match with given match id
 - Request Arguments: Id of match we want to delete,
   example: '/matches/5' will delete match with id=5
 - Response:  JSON object that contains:
     - success state (True) - means everything is ok
     - match id: Id of match that is just deleted
     - message: short message that describes what just happened
Response Example:
```
{
    "match_id": 2,
    "message": "Match deleted successfully",
    "success": true
}
```
### for type of data needed to be inserted in database please look file models.py
