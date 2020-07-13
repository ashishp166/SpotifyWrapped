import os, sys, json, webbrowser
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
from simplejson import JSONDecodeError

def short_term(spotifyObject):
    shorttermtracks = [[0 for x in range(2)] for y in range(50)]
    results = spotifyObject.current_user_top_tracks(time_range='short_term', limit=50)
    for i, item in enumerate(results['items']):
        shorttermtracks[i][0] = item['name']
        shorttermtracks[i][1] = item['artists'][0]['name']
    return shorttermtracks

def medium_term(spotifyObject):
    mediumtermtracks = [[0 for x in range(2)] for y in range(50)]
    results = spotifyObject.current_user_top_tracks(time_range='medium_term', limit=50)
    for i, item in enumerate(results['items']):
        mediumtermtracks[i][0] = item['name']
        mediumtermtracks[i][1] = item['artists'][0]['name']
    return mediumtermtracks

def long_term(spotifyObject):
    longtermtracks = [[0 for x in range(2)] for y in range(50)]
    results = spotifyObject.current_user_top_tracks(time_range='long_term', limit=50)
    for i, item in enumerate(results['items']):
        longtermtracks[i][0] = item['name']
        longtermtracks[i][1] = item['artists'][0]['name']
    return longtermtracks

def short_artist(spotifyObject):
    shorttermartist = [ None for y in range( 50 ) ]
    results = spotifyObject.current_user_top_artists(time_range='short_term', limit=50)
    for i, item in enumerate(results['items']):
        shorttermartist[i] = item['name']
    return shorttermartist

def medium_artist(spotifyObject):
    mediumtermartist = [ None for y in range( 50 ) ]
    results = spotifyObject.current_user_top_artists(time_range='medium_term', limit=50)
    for i, item in enumerate(results['items']):
        mediumtermartist[i] = item['name']
    return mediumtermartist

def long_artist(spotifyObject):
    longtermartist = [ None for y in range( 50 ) ]
    results = spotifyObject.current_user_top_artists(time_range='long_term', limit=50)
    for i, item in enumerate(results['items']):
        longtermartist[i] = item['name']
    return longtermartist