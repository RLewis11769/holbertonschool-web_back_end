# Basic Authentication

## Tasks

### 1
- Add error handler and endpoint for 401 (not found) status code
	- Affected files:
		- api/v1/app.py
		- api/v1/views/index.py
	- Example command:
		- API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
			- curl "http://0.0.0.0:5000/api/v1/unauthorized"
				- Unauthorized

### 2
- Add error handler and endpoint for 403 (unauthorized) status code
	- Affected files:
		- api/v1/app.py
		- api/v1/views/index.py
	- Example command:
		- API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
			- curl "http://0.0.0.0:5000/api/v1/forbidden"
				- Forbidden

### 3
- Create class to manage API authentication
- Add require_auth, authorization_header, and current_user methods
	- Affected files:
		- api/v1/auth/auth.py
	- Used with:
		- API_HOST=0.0.0.0 API_PORT=5000 ./3main.py

### 4
- Update require_auth to check if given path in excluded paths (slash tolerant)
- Meaning path=/api/v1/status and path=/api/v1/status/ must return False if excluded_paths contains /api/v1/status/
	- Affected files:
		- api/v1/auth/auth.py
	- Used with:
		- API_HOST=0.0.0.0 API_PORT=5000 ./4main.py

### 5
- Validate requests to secure API
- Update authorization_header to return value of header request
- Load and assign correct instance of authentication based on global AUTH_TYPE
- Filter requests with before_request
- Add ['/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/'] as excluded paths
	- Affected files:
		- api/v1/app.py
		- api/v1/auth/auth.py
	- Example command:
		- API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=auth python3 -m api.v1.app
			- curl "http://0.0.0.0:5000/api/v1/status"
				- OK
			- curl "http://0.0.0.0:5000/api/v1/status/"
				- OK
			- curl "http://0.0.0.0:5000/api/v1/users"
				- Unauthorized
			- curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Test"
				- Forbidden

### 6
- Create BasicAuth class that inherits from Auth
- Load and assign correct instance of authentication based on global AUTH_TYPE
	- Affected files:
		- api/v1/app.py
		- api/v1/auth/basic_auth.py
	- Example command:
		- API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth python3 -m api.v1.app
			- Same commands and results as 5

### 7
- Return Base64 part of auth header string that starts with "Basic "
- Add extract_base64_authorization_header method
	- Affected files:
		- api/v1/auth/basic_auth.py
	- Used with:
		- API_HOST=0.0.0.0 API_PORT=5000 ./7main.py

### 8
- Return decoded value of Base64 string as string
- Use .decode('utf-8') and try/except
- Add decode_base64_authorization_header method
	- Affected files:
		- api/v1/auth/basic_auth.py
	- Used with:
		- API_HOST=0.0.0.0 API_PORT=5000 ./8main.py

### 9
- Return user email and password from Base64 decoded value
- Note that email/password are passed in string in form of "email:password"
- Add extract_user_credentials method
	- Affected files:
		- api/v1/auth/basic_auth.py
	- Used with:
		- API_HOST=0.0.0.0 API_PORT=5000 ./9main.py

### 10
- Return User instance based on email and password
- Add user_object_from_credentials method
- Logic: Search for user with email and check if pw goes with user who has email
	- Use search class method in models/base.py
	- Use is_valid_password method in models/user.py
	- Use try/catch to verify that user with email exists in first place
	- Affected files:
		- api/v1/auth/basic_auth.py
	- Used with:
		- API_HOST=0.0.0.0 API_PORT=5000 ./10main.py

### 11
- Retrieve user instance for given request
- When given authorization_header, return associated user based on email/pw
- Combine authorization_header method and methods created in 7, 8, 9, and 10
- Note: After run main, user object saved to .db_User.json
- Add current_user method
	- Affected files:
		- api/v1/auth/basic_auth.py
	- Used with:
		- API_HOST=0.0.0.0 API_PORT=5000 ./11main.py
	- Example command:
		- API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth python3 -m api.v1.app
			- curl "http://0.0.0.0:5000/api/v1/status"
				- OK
			- curl "http://0.0.0.0:5000/api/v1/users"
				- Unauthorized
			- curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Basic test"
				- Forbidden
			- curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh"
				- [{"created_at": "datetime", "email": "bob@hbtn.io", "first_name": null, "id": "id", "last_name": null, "updated_at": "datetime"}]

## Server Setup

1. Make sure all required programs are installed:

```
pip3 install -r requirements.txt
```

2. Start the server-side server in one terminal

```
API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```

3. In another terminal, make sure the server is running:

```
curl "http://0.0.0.0:5000/api/v1/status" -vvv
```
