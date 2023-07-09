from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from datetime import timedelta
import json
from os import environ as env
from urllib.parse import quote_plus, urlencode
from authlib.integrations.flask_client import OAuth
from dotenv import find_dotenv, load_dotenv
from functools import wraps

app = Flask(__name__)
app.secret_key = 'SECRET_KEY'
app.debug = True
app.config['SESSION_TYPE'] = 'filesystem'

oauth = OAuth(app)
AUTH_BASE_URL = 'https://dev-bxs7u3fc60nt3h25.us.auth0.com'

auth0 = oauth.register(
    'auth0',
    client_id='OJU36uYZ5h6KZrpggqUklbzhx8bg7nE4',
    client_secret='JsgYk1AE9GdwHKzcgVfXCBoC0MUA7aywLbHRYnFgeFpYDHQvXwQvS4UtvS9ZNeHO',
    api_base_url=AUTH_BASE_URL,
    access_token_url=AUTH_BASE_URL + "/oauth/token",
    authorize_url=AUTH_BASE_URL + "/authorize",
    client_kwargs={
        'scope': 'openid profile email',
        'redirect_uri': 'http://localhost:8000/callback'
    },
    server_metadata_url=AUTH_BASE_URL + '/.well-known/openid-configuration'
)


class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


def request_auth(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        if 'user' not in session:
            return redirect('/home')
        return func(*args, **kwargs)
    return decorated


@app.route('/home')
def home():
    print('home route')
    return render_template('home.html')


@app.route('/login')
def login():
    return auth0.authorize_redirect(return_to=url_for('callback', _external=True, _scheme='https'))


@app.route('/callback', methods=['GET', 'POST'])
def callback():
    token = auth0.authorize_access_token()
    print(token)
    session['user'] = token
    return redirect(url_for('dashboard'))


@app.route('/dashboard')
@request_auth
def dashboard():
    return render_template('dashboard.html', session=session.get('user'), pretty=json.dumps(session.get('user'), indent=4))


@app.route('/settings')
@request_auth
def settings():
    if 'access_token' in session['user']:
        resp = auth0.get('userinfo')
        if resp.status_code == 200:
            session['nickname'] = resp.json()['nickname']
            return render_template('settings.html', picture=resp.json()['picture'])
        else:
            return 'Error fetching user info from Auth0', 500
    else:
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8000)
