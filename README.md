# SpotifyWrapped


A project built on flask to let people explore new artists and see their top artists and songs. There are couple other features included in the project such as the song currently playing and new songs out. 

Project uses the [Spotipy api](https://spotipy.readthedocs.io/en/2.13.0/) to get the listening history and discover new artists and music.

## How To Use

Changes to file:
<br />
1. Set up a developer account in [Spotify Dashboard](https://developer.spotify.com/dashboard/)

2. Create an app in the dashboard and get the client ID and the client secret ID over to the data python file at the indicated 'xxxxxxx' portion.

3. Go to your spotify account and copy your profile link and add the userID below the client and secret id.

4. Download the dependencies and run the app.

```
# Install dependencies
pip install spotipy
pip install json
```

```
# Run app
python3 server.py
```
---
