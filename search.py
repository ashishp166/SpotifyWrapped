import os, sys, webbrowser
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
import json as simplejson
from simplejson import JSONDecodeError

def artists(searchinput, spotifyObject):
    searchResults = spotifyObject.search(searchinput,1,0,"artist")
    artist = searchResults['artists']['items'][0]
    return artist

def artistname(inputvalue, spotifyObject):
    value = artists(inputvalue, spotifyObject)
    artistName = value['name']
    return artistName

def artistfollower(inputvalue, spotifyObject):
    value = artists(inputvalue, spotifyObject)
    artistfollowers = value['followers']['total']
    return artistfollowers

def genre(inputvalue, spotifyObject):
    value = artists(inputvalue, spotifyObject)
    artistfollowers = value['genres'][0]
    return artistfollowers

def album(inputvalue, spotifyObject):
    value = artists(inputvalue, spotifyObject)
    #webbrowser.open(value['images'][0]['url'])
    artistID = value['id']
    trackURIs = []
    trackArt = []
    albumnumber = 0
    tracknumber = 0
    albumname = [] 

    # Extract album data
    albumResults = spotifyObject.artist_albums(artistID)
    albumResults = albumResults['items']

    for item in albumResults:
        trackname = []
        trackname.append(item['name'])
        albumID = item['id']
        albumArt = item['images'][0]['url']

        # Extract track data
        trackResults = spotifyObject.album_tracks(albumID)
        trackResults = trackResults['items']

        for item in trackResults:
            trackname.append(item['name'])
            trackURIs.append(item['uri'])
            trackArt.append(albumArt)
            tracknumber+=1
        albumnumber+=1
        albumname.append(trackname)
    return albumname

def albumartwork():
    # See album art
    while True:
        songSelection = input("Enter a song number to see album art and play the song (x to exit): ") # and play the song
        if songSelection == "x":
            break
        trackSelectionList = []
        trackSelectionList.append(trackURIs[int(songSelection)])
        spotifyObject.start_playback((currentDevice), None, trackSelectionList) # added
        webbrowser.open(trackArt[int(songSelection)])