from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@app.route('/Mustaeen')
def name():
    return "Hello, Mustaeen!"

# https://flask.palletsprojects.com/en/3.0.x/quickstart/#a-minimal-application