# Session Authentication

## Tasks

### 0
- Copy 0x03-Basic_authentication into this folder
- Assign result of auth.current_ser(request) to request.current_user
- Update route method to use request.current_user

### 1
- Create SessionAuth class that inherits from Auth
- Load and assign correct instance of authentication based on global AUTH_TYPE

### 2
- Add class attribute user_id_by_session_id initialized by empty dict
- Add create_session method to create session ID

### 3
- Add user_id_for_session_id method to retrn user ID based on given session ID

### 4
- Add session_cookie method to return cookie value from request

### 5
- Update before_request method to add /api/v1/auth_session/login/ to list of excluded paths

### 6
- Add current_user method to return user instance based on cookie value

### 7
- Create new Flask view that handles all routes for session authentication

### 8
- Add destroy_session method that deletes user session and logs out
