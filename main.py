import os, sys, json, webbrowser
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
from simplejson import JSONDecodeError

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

if artist != "":
    print("Currently playing " + artist + " - " + track)
else:
    print("nothing is playing right now")

# User information
user = spotifyObject.current_user()
displayName = user['display_name']
followers = user['followers']['total']

# Loop
while True:
    # Main Menu
    print()
    print(">>> Welcome to Spotipy " + displayName + "!")
    print(">>> You have " + str(followers) + " followers.")
    print()
    print("0 - Search for an artist")
    print("1 - Top tracks")
    print("2 - exit")
    print()
    choice = input("Your choice: ")

    if choice == "0":
        print()
        searchQuery = input("Ok, what's their name?: ")
        print()

        # Get search results
        searchResults = spotifyObject.search(searchQuery,1,0,"artist")

        # Artist details
        artist = searchResults['artists']['items'][0]
        print(artist['name'])
        print(str(artist['followers']['total']) + " followers")
        print(artist['genres'][0])
        print()
        webbrowser.open(artist['images'][0]['url'])
        artistID = artist['id']


        # Album and track details
        trackURIs = []
        trackArt = []
        z = 0

        # Extract album data
        albumResults = spotifyObject.artist_albums(artistID)
        albumResults = albumResults['items']

        for item in albumResults:
            print("ALBUM: " + item['name'])
            albumID = item['id']
            albumArt = item['images'][0]['url']

            # Extract track data
            trackResults = spotifyObject.album_tracks(albumID)
            trackResults = trackResults['items']

            for item in trackResults:
                print(str(z) + ": " + item['name'])
                trackURIs.append(item['uri'])
                trackArt.append(albumArt)
                z+=1
            print()

        # See album art
        while True:
            songSelection = input("Enter a song number to see album art and play the song (x to exit): ") # and play the song
            if songSelection == "x":
                break
            trackSelectionList = []
            trackSelectionList.append(trackURIs[int(songSelection)])
            spotifyObject.start_playback((currentDevice), None, trackSelectionList) # added
            webbrowser.open(trackArt[int(songSelection)])

    if choice == "1":
        ranges = ['short_term', 'medium_term', 'long_term']
        while True:
            print("Enter one of the numbers for the following range lengths:\n 1)4 weeks \n 2)6 months \n 3)lifetime\n")
            rangelength = int(input("Your choice: "))
            print("range:", ranges[rangelength-1])
            results = spotifyObject.current_user_top_tracks(time_range=ranges[rangelength-1], limit=50)
            for i, item in enumerate(results['items']):
                print(i+1, item['name'], '//', item['artists'][0]['name'])
            print()
    
    if choice == "2":
        break
