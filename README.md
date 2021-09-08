# Coffee Shop Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Environment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/starter` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server

From within the `./starter` directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=app.py;
```

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## Tasks

### Setup Auth0

1. Create a new Auth0 Account
2. Select a unique tenant domain
3. Create a new, single page web application
4. Create a new API
   - in API Settings:
     - Enable RBAC
     - Enable Add Permissions in the Access Token
5. Create new API permissions:
   - `get:movies-detail`
   - `post:movies`
   - `patch:movies`
   - `delete:movies`
   *************
   - `get:get:actor-detail`
   - `post:actors`
   - `patch:actors`
   - `delete:actors`
6. Create new roles for:
   - Actor
     - can `get:movies-detail`
   - Manager
     - can perform all actions
7. Test your endpoints with [Postman](https://getpostman.com).
   - Register 2 users - assign the Barista role to one and Manager role to the other.
   - Sign into each account and make note of the JWT.
   - Import the postman collection `./starter/udacity-fsnd-udaspicelatte Copy.postman_collection.json`
   - Right-clicking the collection folder for barista and manager, navigate to the authorization tab, and including the JWT in the token field (you should have noted these JWTs).
   - Run the collection and correct any errors.
   - Export the collection overwriting the one we've included so that we have your proper JWTs during review!


## APIs
```js
GET '/Movies' OR '/movies-detail'
- Fetches a dictionary of Movies in which the keys are the ids 
- Request Arguments: None
- Returns: An object with a single key, Movies, that contains an object of id: Movies_string key:value pairs. 
{
    'movies': { 
    '1' : "14430104",
    '2' : "14450125",
    '3' : "14450125"
     }

}
```
```js
GET '/Actor' OR '/actor-detail'
- Fetches a dictionary of Actor in which the keys are the ids
- Request Arguments: None
- Returns: An object with a single key, Actor, that contains an object of id: Actor_string key:value pairs. 
{
    'Actors': { 
    'id' : "1",
    'name' : "Jennifer Aniston",
    'age' : "40",
    'gender' : "female"
     }
}
```


```js
POST '/movies'
- Sends a post request in order to add a new movies
- Request Body: 
{
    'releaseDate':  'Heres a new releaseDate string',

}
- Returns: Does not return any new data
```

```js
POST '/actors'
- Sends a post request in order to add a new actors
- Request Body: 
{
    'name' = 'Heres a new name string'
    'age' = 'Heres a new age string'
    'gender' = 'Heres a new gender string'

}
- Returns: Does not return any new data
```

```js
DELETE '/actors/<int:id>'
- Send a id  to delete a actor 

- Returns: {'success': True, 'delete': id}
```
```js
DELETE '/movies/<int:id>'
- Send a id  to delete a movie 

- Returns: {'success': True, 'delete': id}
```
