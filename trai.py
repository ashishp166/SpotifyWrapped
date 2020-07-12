import os, sys, json, webbrowser
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
#from json.decoder import JSONDecodeError

#information that needs to be changed
os.environ['client_id'] = '852da567ab954f35a9da1a6a22ee6b0e'
os.environ['client_secret'] = '6988c5d09d30417cb485ad95260558dc'
os.environ['user'] = '31sdqm5miqstsicwf3aq3prku3le?si=zPV-FQ6aRM6LPV3w2e2Rug'

#other inforamtion for creating a token
scope = 'user-read-private user-read-playback-state user-modify-playback-state user-top-read'
os.environ['redirect_uri'] = 'http://localhost:2000/callback'

#getenv
myClientId = os.getenv('client_id')
mySecret = os.getenv('client_secret')
myRedirect = os.getenv('redirect_uri')
username = os.getenv('user')
warriors = 5


# Erase cache and prompt for user permission
try:
    token = util.prompt_for_user_token(username, scope, myClientId, mySecret, myRedirect)
except (AttributeError, JSONDecodeError):#*
    os.remove('user')
    token = util.prompt_for_user_token(username, scope)

# Create our spotify object with permissions
spotifyObject = spotipy.Spotify(auth=token)

# Get current device
Spotifydevices = spotifyObject.devices()
currentDevice = Spotifydevices['devices'][0]['id']

# Current track information
track = spotifyObject.current_user_playing_track()
artist = track['item']['artists'][0]['name']
track = track['item']['name']


# User information
user = spotifyObject.current_user()
displayName = user['display_name']
followers = user['followers']['total']

 