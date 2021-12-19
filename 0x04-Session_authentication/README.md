# Session Authentication

## Description

In this project, you will implement a Session Authentication. You are not allowed to install any other module.

In the industry, you should NOT implement your own Session authentication system and should instead use a module or framework that does it for you (like in Python-Flask: [Flask-HTTPAuth](https://flask-httpauth.readthedocs.io/en/latest/)). Here, for learning purposes, we will walk through each step of this mechanism to understand it better by doing.

## Tasks

### 0
- Copy 0x03-Basic_authentication into this folder
- Updates view_one_user to add if checks for user_id == 'me' as stand-in for current user
- Assigns auth.current_user(request) to request.current_user
- Updates before_request to use request.current_user
	- Affected files:
		- api/v1/app.py
		- api/v1/views/users.py
	- Used with:
		- API_HOST=0.0.0.0 API_PORT=5000 ./0main.py
	- Example command:
		- API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth python3 -m api.v1.app
			- curl "http://0.0.0.0:5000/api/v1/status"
				- OK
			- curl "http://0.0.0.0:5000/api/v1/users"
				- Unauthorized
			- curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh"
				- - [{"created_at": "datetime", "email": "bob@hbtn.io", "first_name": null, "id": "id", "last_name": null, "updated_at": "datetime"}]
			- curl "http://0.0.0.0:5000/api/v1/users/me" -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh"
				- Same as above

### 1
- Creates SessionAuth class that inherits from Auth
- Loads and assigns correct instance of authentication based on global AUTH_TYPE
	- Affected files:
		- api/v1/app.py
		- api/v1/auth/session_auth.py
	- Example command:
		- curl "http://0.0.0.0:5000/api/v1/status"
			- OK
		- curl "http://0.0.0.0:5000/api/v1/users"
			- Unauthorized
		- curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Test"
			- Forbidden

### 2
- Adds class attribute user_id_by_session_id initialized by empty dict
- Adds create_session method to return session ID
- Creates session ID and set as key in user_id_by_session_id dict with user ID value
	- Affected files:
		- api/v1/auth/session_auth.py
	- Used with:
		- API_HOST=0.0.0.0 API_PORT=5000 ./2main.py

### 3
- Adds user_id_for_session_id method to retrn user ID based on given session ID
- Using user_id_by_session_id class dict
	- Affected files:
		- api/v1/auth/session_auth.py
	- Used with:
		- API_HOST=0.0.0.0 API_PORT=5000 ./3main.py

### 4
- Updates auth.py with session_cookie method
- Returns session ID value from cookie dict based on env variable
	- Affected files:
		- api/v1/auth/auth.py
	- Used with:
		- API_HOST=0.0.0.0 API_PORT=5000 ./4main.py
	- Example command:
		- curl "http://0.0.0.0:5000"
			- None
		- curl "http://0.0.0.0:5000" --cookie "_my_session_id=Hello"
			- Hello

### 5
- Updates before_request method to add /api/v1/auth_session/login/ to list of excluded paths
- Adds if check to before_request
	- Affected files:
		- api/v1/app.py
	- Example command:
		- API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth SESSION_NAME=_my_session_id python3 -m api.v1.app
			- curl "http://0.0.0.0:5000/api/v1/status"
				- OK
			- curl "http://0.0.0.0:5000/api/v1/auth_session/login"
				- Not found
			- curl "http://0.0.0.0:5000/api/v1/users/me"
				- Unauthorized
			- curl "http://0.0.0.0:5000/api/v1/users/me" -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh"
				- Forbidden (environment variable AUTH_TYPE is equal to "session_auth" so need more info - this would work for basic)
			- curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=5535d4d7-3d77-4d06-8281-495dc3acfe76"
				- Forbidden (no user if linked to session ID)

### 6
- Adds current_user method to return user instance based on request
- Can get session id with cookie request, user id with session id, and user object with user id
	- Affected files:
		- api/v1/auth/session_auth.py
	- Used with:
		- API_HOST=0.0.0.0 API_PORT=5000 ./6main.py
	- Example command:
		- curl "http://0.0.0.0:5000/" --cookie "_my_session_id=Holberton"
			- No user found
		- curl "http://0.0.0.0:5000/" --cookie "_my_session_id=SESSION ID"
			- User found
				- Main file will print session ID string to test with

### 7
- Creates new Flask view that handles all routes for session authentication (as in login)
- Retrieves data from request object and create new session based on data
- Sets cookie to response with value of session ID
- Returns response with jsonified dict representation of user
- Adds view to package
	- Affected files:
		- api/v1/views/session_auth.py
		- api/v1/views/__init__.py
	- Example command:
		- API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth SESSION_NAME=_my_session_id python3 -m api.v1.app
			- curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XPOST
				- email missing
			- curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XPOST -d "email=guillaume@hbtn.io"
				- password missing
			- curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XPOST -d "email=guillaume@hbtn.io" -d "password=test"
				- no user found for this email
			- curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XPOST -d "email=bobsession@hbtn.io" -d "password=test"
				- wrong password
			- curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XPOST -d "email=bobsession@hbtn.io" -d "password=fake pwd" -vvv
				- Successful user object
				- Info will include:
					- Set-Cookie: _my_session_id=SESSION ID; Path=/

### 8
- Add destroy_session method that deletes session ID from user_id_by_session_id
- Creates new Flask view that handles all routes for session deletion (as in logout)
	- Affected files:
		- api/v1/auth/session_auth.py
		- api/v1/views/session_auth.py
	- Example command:
		- API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth SESSION_NAME=_my_session_id python3 -m api.v1.app
			- curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XPOST -d "email=bobsession@hbtn.io" -d "password=fake pwd" -vvv (use session ID as found in Set-Cookie: _my_session_id=SESSION ID for next curls)
			- curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=SESSION ID"
				- User obj info
			- curl "http://0.0.0.0:5000/api/v1/auth_session/logout" --cookie "_my_session_id=SESSION ID" -XDELETE
				- {}
			- curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=SESSION ID"
				- Forbidden

## Setup

In one terminal run:

```
API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth python3 -m api.v1.app
```

While that terminal is still running, in second terminal run:

```
$ curl "http://0.0.0.0:5000/api/v1/status"
{ "status": "OK" }
```

## Learning Objectives

- What authentication means
- What session authentication means
- What Cookies are
- How to send Cookies
- How to parse Cookies
