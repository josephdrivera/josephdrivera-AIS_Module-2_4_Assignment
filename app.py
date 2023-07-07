from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from datetime import timedelta
import json
from os import environ as env
from urllib.parse import quote_plus, urlencode
from authlib.integrations.flask_client import OAuth
from dotenv import find_dotenv, load_dotenv
from functools import wraps

app = Flask(__name__)
oauth = OAuth(app)
app.secret_key = env.get('SECRET_KEY')
app.debug = True
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
        'redirect_uri': 'http://localhost:5000/callback'
    },
    server_metadata_url=AUTH_BASE_URL + '/.well-known/openid-configuration'
)

app.config['SESSION_TYPE'] ='filesystem'

class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code
        