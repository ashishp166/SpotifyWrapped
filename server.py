import os
from flask import Flask, redirect, url_for, render_template, request
from data import *
from search import *
from lisentingHistory import *
import os, sys, json, webbrowser
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
from simplejson import JSONDecodeError

app = Flask(__name__)

#@app.route("/")
#def index():
    #return render_template("index.html", message="Hello Flask!", contacts = ['c1', 'c2', 'c3', 'c4', 'c5'])

@app.route("/currentsong")
def index1():
    return render_template('currentsong.html', artist=artist, track=track)

@app.route("/home")
def menu():
    return render_template('menu.html', name = displayName, followers=followers)

@app.route("/search", methods=["POST", "GET"])
def search():
    if request.method == "POST":
        user = request.form["searching"]
        return redirect(url_for('result', resultFound = user))
    else:
        return render_template("search.html")

@app.route("/<resultFound>")
def result(resultFound):
    #return f"<h1>{user}</h1>"
    return render_template('result.html', nameartist = artistname(resultFound, spotifyObject), numfollowers = artistfollower(resultFound, spotifyObject), genre = genre(resultFound, spotifyObject), album = album(resultFound, spotifyObject))

@app.route("/toptrack")
def toptrack():
    return render_template('toptrack.html', short = short_term(spotifyObject), medium = medium_term(spotifyObject), long = long_term(spotifyObject))

@app.route("/topartist")
def topartist():
    return render_template('topartist.html', short = short_artist(spotifyObject), medium = medium_artist(spotifyObject), long = long_artist(spotifyObject))

@app.route("/")
def homepage():
    return render_template('homepage.html', name = displayName, followers=followers)

if __name__ == "__main__":
    app.run(debug=True)