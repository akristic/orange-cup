# Orange Cup
 Udacity Capstone Project for Full stack ND
 -----

 ### Introduction

 Orange cup is tennis web app for keeping score of tennis matches. It is a backend API created for Udacity Capstone Project for Full stack ND. This is backend for site that allows user to login, create players and matches and share them with the world. My motivation for this project is that after completing this Nanodegree I will continue to work on this project and make professional web site that will be connected with android app Orange Cup.


#### Virtual Enviornment

It is recommended working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/` root directory and running:

```bash
pip install -r requirements.txt
```

## Running the server

From within the root directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application.

# For testing endpoints in postman you will need VALID token.
This token will be provided to Udacity in submission. (2 Tokens. One for User and one for Admin)

To get your own tokens you will need to make your own account on Auth0. And in auth/auth.py file you will need to change
AUTH0_DOMAIN = 'orangecup.auth0.com'
API_AUDIENCE = 'orange'
to values from your account.
There are 2 roles setup:
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

After successfully login you will be redirected to login-result page but because there is no frontend you will land on This site can’t be reached page. Just copy token from url created in your browser. It will look something like this:
```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ikxza1ZQMGtWOXpMSGhUU1pzSDRXeCJ9.eyJpc3MiOiJodHRwczovL29yYW5nZWN1cC5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTE3OTMyNzA5MTk5MDIxODI0MzciLCJhdWQiOlsib3JhbmdlIiwiaHR0cHM6Ly9vcmFuZ2VjdXAuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTU4NzcwNDk4OSwiZXhwIjoxNTg3NzEyMTg5LCJhenAiOiJmWFdmNXJlTmx5TVNncTRUanhRMjN2dmh0WUZyWnpzViIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6bWF0Y2hlcyIsImRlbGV0ZTpwbGF5ZXJzIiwiZGVsZXRlOnNldHRpbmdzIiwicmVhZDptYXRjaGVzIiwicmVhZDpwbGF5ZXJzIiwicmVhZDpzZXR0aW5ncyIsIndyaXRlOm1hdGNoZXMiLCJ3cml0ZTpwbGF5ZXJzIiwid3JpdGU6c2V0dGluZ3MiXX0.jmce8wwNdsNo3xWSdhvqHEyKsbWYxNpMzzCbCswnhawRxDhEMHk-TifslD3jMwcs77X_89isVsed4upT2yQtSu_xpK2GskInTdtxffycoctD-d9AFpu67NphPtZDUZjw_ay0hhYaLrmvLBCelTkS6u4P2TuxpeL3rI5nb_zUhFaqwsB8a4kkUvAk0UOhX1jxLCXxyifjZH4KtQ7MtkFpG3hZ842QYlo12wv5N3frfenFlVHNQMGC2Y2Jr1dAqD_RUQDYjE0babTbukSxjRoYXLmx2okrU3K-o--EoarztWOgFjSSq_b6LkrZHiSBnoAkx7YNU3nC9FIRpbifCDx6cA
```
# Testing with Postman
Import collection in postman from file: orange-cup-endpoint-test-collection.postman_collection
In postman under Authorization tab select Type of authorization to OAuth 2.0. Use newly created token and paste it in Access Token box.
Important: You must have database "orange" created and populated with some dummy data. Run all post test under admin folder to populate database. Do this few times to have few rows in database.
