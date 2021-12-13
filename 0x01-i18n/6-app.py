#!/usr/bin/env python3
""" Routes and config """
from flask import Flask, g, render_template, request
from flask_babel import Babel

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
    # 1. URL parameters
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    try:
        user = get_user()
        # 2. User settings
        if user and user['locale'] and user['locale'] in app.config['LANGUAGES']:
            return user['locale']
    except Exception:
        return request.accept_languages.best_match(Config.LANGUAGES)


def get_user():
    """ Get user from request header """
    id = request.args.get('login_as')
    try:
        return users.get(int(id))
    except Exception:
        return None


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
