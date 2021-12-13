#!/usr/bin/env python3
""" Routes and config """
from flask import Flask, g, render_template, request
from flask_babel import Babel
from pytz import timezone, UnknownTimeZoneError

app = Flask(__name__)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """ App configuration """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    Locale selector to determine language to use on templates

    Priority:
        1. URL parameters
        2. User settings
        3. Request header
        4. Default locale
    """
    loc = request.args.get('locale')
    # 1. URL parameters
    if loc and loc in app.config['LANGUAGES']:
        return loc
    try:
        user = get_user()
        # 2. User settings
        if user and user['loc'] and user['loc'] in app.config['LANGUAGES']:
            return user['loc']
    except Exception:
        # Else will fall to here if user is not logged in for 3. Request header
        # Also 4. Default locale
        return request.accept_languages.best_match(Config.LANGUAGES)


def get_user():
    """ Get user from request header """
    id = request.args.get('login_as')
    try:
        # Parse login_as=id as int
        return users.get(int(id))
    except Exception:
        return None


@babel.timezoneselector
def get_timezone():
    """
    Timezone selector to determine timezone
    Make sure timezone is valid - invalid are skipped to try next priority

    Priority:
        1. URL parameters
        2. User settings
        3. Default timezone
    """
    tz = request.args.get('timezone')
    if tz:
        # 1. URL parameters
        try:
            timezone(tz)
            return tz
        except UnknownTimeZoneError:
            pass
    if g.user:
        user_tz = g.user.get('timezone')
        if user_tz:
            # 2. User settings
            try:
                timezone(user_tz)
                return user_tz
            except UnknownTimeZoneError:
                pass
    # 3. Default timezone
    return Config.BABEL_DEFAULT_TIMEZONE


@app.before_request
def before_request():
    """ Before request to stash user in global """
    g.user = get_user()


@app.route("/", methods=['GET'])
def index():
    """ Index route """
    return render_template("6-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
