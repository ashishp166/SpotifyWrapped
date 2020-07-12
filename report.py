from flask import render_template
import os, sys, json, webbrowser
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
#from json.decoder import JSONDecodeError
from trai import *
from flask import Flask 

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html', artist=artist, track=track)

@app.route('/about')
def hello_world():
    return render_template('hello.html')


if __name__ == "__main__":
    app.run()