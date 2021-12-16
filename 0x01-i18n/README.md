# Starts with I then 18 characters and ends in N
# Internationalization

## Requirements

Make sure Babel installed with:
```
pip3 install flask_babel
```

## Mandatory

### 0-app.py
- Create basic Flask app with hardcoded title/h1 info
	- Affected files:
		- templates/0-index.html

### 1-app.py
- Instantiate Babel object with default locale and timezone
- Configure ["en", "fr"] as languages

### 2-app.py
- Add get_locale function
- Use request.accept_languages to determine default language

### 3-app.py
- Parameterize templates
- Edit .po files to provide correct value for basic message IDs
- Update template to include translation texts
	- Affected files:
		- templates/3-index.html
		- babel.cfg (specifically told what to add to configure)
		- translations/**/LC_MESSAGES/messages.mo - en/fr
		- translations/**/LC_MESSAGES/messages.po - en/fr
	- Relevant commands:
		- pybabel extract -F babel.cfg -o messages.pot .
			- Initialize translations
		- pybabel init -i messages.pot -d translations -l en
		- pybabel init -i messages.pot -d translations -l fr
			- Initialize dictionaries
		- pybabel compile -d translations
			- Compile dictionaries

### 4-app.py
- Update get_locale function to include URL parameters
- Meaning detect if URL says http://127.0.0.1:5000/?locale=fr

### 5-app.py
- Mock logging in with URL parameters, using data in users table
- Add get_user function to return user dictionary for given user when URL says http://127.0.0.1:5000/?login_as=2
- Add before_request to add found user to global scope with flask.g.user
- Update .po files to provide correct value for message IDs with variable
- Update template to include translation texts with variables using data stored in g.user
	- Affected files:
		- templates/5-index.html
		- translations/**/LC_MESSAGES/messages.mo - en/fr
		- translations/**/LC_MESSAGES/messages.po - en/fr
	- Relevant commands:
		- pybabel compile -d translations
			- Compile dictionaries

### 6-app.py
- Update get_locale to set order of priority to find user's locale

### 7-app.py
- Add get_timezone function using @babel.timezoneselector decorator
- Set order of priority to find user's timezone
- Including detecting if URL says http://127.0.0.1:5000/?timezone=cst
- Validate that given timezone exists with pytz.timezone, catching UnknownTimeZoneError exception

## Advanced

### app.py
- Add current time to index page
- Use format_datetime to provide proper format and pass to template
- Update .po files to provide correct value for message ID with variable
- Update template to include translation texts with variables using data passed to template
	- Affected files:
		- templates/index.html
		- translations/**/LC_MESSAGES/messages.mo - en/fr
		- translations/**/LC_MESSAGES/messages.po - en/fr
	- Relevant commands:
		- pybabel compile -d translations
			- Compile dictionaries

## Learning Objectives

- Learn how to parametrize Flask templates to display different languages
- Learn how to infer the correct locale based on URL parameters, user settings or request headers
- Learn how to localize timestamps
