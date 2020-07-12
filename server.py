import os
from flask import Flask, redirect, url_for, render_template, request
from trai import *
from search import *
import os, sys, json, webbrowser
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
from simplejson import JSONDecodeError

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", message="Hello Flask!", contacts = ['c1', 'c2', 'c3', 'c4', 'c5'])

@app.route("/about")
def index1():
    return render_template('index1.html', artist=artist, track=track)

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

if __name__ == "__main__":
    app.run(debug=True)