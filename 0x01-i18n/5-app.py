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


def get_user():
    """ Get user from request header """
    id = request.args.get('login_as')
    try:
        # Parse login_as=id as int
        return users.get(int(id))
    except Exception:
        return None


@app.before_request
def before_request():
    """ Before request to stash user in global """
    g.user = get_user()


@babel.localeselector
def get_locale():
    """ Locale selector to determine language to use on templates """
    loc = request.args.get('locale')
    # URL parameters aka ?locale=fr
    if loc and loc in app.config['LANGUAGES']:
        return loc
    # Default locale
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route("/", methods=['GET'])
def index():
    """ Index route """
    return render_template("6-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
