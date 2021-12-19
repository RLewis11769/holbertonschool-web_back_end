# User Authentication

## Description

In the industry, you should not actually implement your own authentication system and should instead use a module or framework that does it for you (like [Flask-User](https://flask-user.readthedocs.io/en/latest/) or [FlaskLogin](https://pythonbasics.org/flask-login/)). This project walks through each step of user authentication to understand it by doing.

## Task Files

- auth.py
	- Interacts with authentication database
	- Uses db.py's methods through self._db
		- Tasks:
			- 4, 5, 8, 9, 10, 12, 13, 16, 18
- app.py
	- Contains Flask app setup and routes
	- Uses auth.py's methods through AUTH
		- Tasks:
			- 6, 7, 11, 14, 15, 17, 19
- db.py
	- Creates database instance
	- Interacts with User class and users table
		- Tasks:
			- 1, 2, 3
- main.py
	- Test file containing functions testing that responses from app.py requests are accurate
		- Tasks:
			- 20 (advanced)
- user.py
	- Defines Users class that "users" table and columns are based on
		- Tasks:
			- 0

## Mandatory Tasks

### 0
- Create SQLAlchemy model User for database table "users" with specified attributes
	- Test with:
		- 0main.py
	- Relevant file:
		- user.py

### 1
- Create DB class to initialize new database instance
- Add DB.add_user method which returns User object based on email/password
	- Test with:
		- 1main.py
	- Relevant file:
		- db.py

### 2
- Add DB.find_user_by method that finds row in users table filtered by (key=value) kwargs
- NoResultFound error when no user with attributes and InvalidRequestError when wrong query args passed
	- Test with:
		- 2main.py
	- Relevant file:
		- db.py

### 3
- Add DB.update_user method that uses find_user_by to find given user, then updates user's attributes based on kwargs using setattr
	- Test with:
		- 3main.py
	- Relevant file:
		- db.py

### 4
- Create _hash_password function that uses bcrypt to return hashed and salted password
	- Test with:
		- 4main.py
	- Relevant file:
		- auth.py

### 5
- Add Auth class to interact with authentication database
- Add Auth.register_user method to return User object based on email/password
	- If user with email exists in database, don't add to database
	- If user doesn't exist, hash password, add to database, and return new User object
	- Test with:
		- 5main.py
	- Relevant file:
		- auth.py

### 6
- Set up basic Flask app
- Defines / GET route that returns hardcoded JSON payload
	- Test on second terminal with:
		```
		$ curl localhost:5000/
		{"message": "Bienvenue"}
		```
	- Relevant file:
		- app.py

### 7
- Create end point to register user
- Define /users POST route that expects email=value and password=value and returns message
- Uses AUTH.register_user method to add to database
- Returns jsonified message based on success/failure of registration
	- Test on second terminal with:
		```
		$ curl -XPOST localhost:5000/users -d 'email=bob@me.com' -d 'password=mySuperPwd' -v
		{"email":"bob@me.com","message":"user created"}
		$ curl -XPOST localhost:5000/users -d 'email=bob@me.com' -d 'password=mySuperPwd' -v
		{"message":"email already registered"}
		```
	- Relevant file:
		- app.py

### 8
- Add Auth.valid_login method that returns T/F based on email and password arguments using bcrypt.checkpw
	- Test with:
		- 8main.py
	- Relevant file:
		- auth.py

### 9
- Add _generate_uuid function that returns random string representation of uuid
	- No testing necessary
	- Relevant file:
		- auth.py

### 10
- Add Auth.create_session method that returns session ID
- Finds user for given email, generates new UUID, updates given user's session ID in database with DB.update_user, and returns
	- Test with:
		- 10main.py
	- Relevant file:
		- auth.py

### 11
- Create end point to log in user
- Define /sessions POST route that expects email=value and password=value
- Returns jsonified message based on success/failure of login
	- If login credentials are correct, create new session, store session ID as cookie, and return JSON message
	- If login unauthorized, abort 401
	- Test on second terminal with:
		```
		$ curl -XPOST localhost:5000/users -d 'email=bob@bob.com' -d 'password=mySuperPwd'
		$ curl -XPOST localhost:5000/sessions -d 'email=bob@bob.com' -d 'password=mySuperPwd' -v
		{"email":"bob@bob.com","message":"user created"}
		$ curl -XPOST localhost:5000/sessions -d 'email=bob@bob.com' -d 'password=BlaBla' -v
		<title>401 Unauthorized</title>
		<h1>Unauthorized</h1>
		```
	- Relevant file:
		- app.py

### 12
- Add Auth.get_user_from_session_id method to return user based on given session ID
	- Use DB.find_user_by to find user based on session ID
	- Relevant file:
		- auth.py

### 13
- Add Auth.destroy_session to update session ID of user associated with given user ID to None
	- Use DB.find_user_by to find user based on ID, then update_user to update session_id
	- Relevant file:
		- auth.py

### 14
- Create end point to log out user
- Define /sessions DELETE route that expects session_id=value
	- If user is associated with session ID, use Auth.destroy_session to remove session ID and redirect to "/"
	- If user doesn't exist, abort 403

	- Relevant file:
		- app.py

### 15
- Create end point to load profile for given user
- Define /profile GET route that expects session_id=value
	- If user is associated with session ID, use Auth.get_user_from_session_id to return jsonified message
	- If session ID doesn't exist, abort 403
	- Test on second terminal with:
		```
		$ curl -XPOST localhost:5000/sessions -d 'email=bob@bob.com' -d 'password=mySuperPwd' -v
			- session_id saved as cookie
		{"email":"bob@bob.com","message":"logged in"}
		$ curl -XGET localhost:5000/profile -b "session_id=SESSION_ID"
		{"email": "bob@bob.com"}
		$ curl -XGET localhost:5000/profile -b "session_id=75c89af8-1729-44d9-a592-41b5e59de9a1"
		<title>403 Forbidden</title>
		<h1>Forbidden</h1>
		```
	- Relevant file:
		- app.py

### 16
- Add Auth.get_reset_password_token method to return uuid based on given email
	- Use DB.find_user_by to find associated user, generate uuid, update user's reset_token field, and return
	- Relevant file:
		- auth.py

### 17
- Create end point to reset password token for given user
- Define /reset_password POST route that expects email=value
	- If email is registered, get token and return jsonified message
	- If email doesn't exist, abort 403
	- Relevant file:
		- app.py

### 18
- Add Auth.update_password method to takes reset_token and new password, then resets user's hashed_password field and clears reset_token field
- Uses DB.find_user_by based on reset_token, _hash_password to hash new password, and DB.update_user to update pw and token fields in database
	- Relevant file:
		- auth.py

### 19
- Create end point to update/reset password for given user
- Define /reset_password PUT route that expects email=value, reset_token=value, and new_password=value
	- If reset_token exists, use Auth.update_password to update hashed_password and reset_token, then return jsonified message containing email (email not necessary to reset)
	- If reset_token doesn't match user, abort 403
	- Relevant file:
		- app.py

## Advanced Task

### 20
- Create test functions to query web server for corresponding end point, and assert returned status code is expected
- Use requests module to query
- If everything is correct, there should be no output from running file
	- Testing:
		- register_user = requests.post for /users (task 7)
		- log_in_wrong_password = requests.post for /sessions (task 11)
		- log_in = requests.post for /sessions (task 11)
		- profile_unlogged = requests.get for /profile (task 15)
		- profile_logged = requests.get for /profile (task 15)
		- log_out = requests.delete for /sessions (task 14)
		- reset_password_token = requests.post for /reset_password (task 17)
		- update_password = requests.put for /reset_password (task 19)
	- Relevant file:
		- main.py

## Setup

1. Make sure bcrypt is installed (originally seen in 0x02-personal data)

2. Move main files into current directory if testing for proper imports

## Learning Objectives

- How to declare API routes in a Flask app
- How to get and set cookies
- How to retrieve request form data
- How to return various HTTP status codes
