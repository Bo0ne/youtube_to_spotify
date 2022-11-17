from googleapiclient.discovery import build
from googleapiclient.discovery import build
import googleapiclient.errors
import re
import tekore as tk

googleAPIkey = input("Enter your GoogleAPI key ")
# Spotify
client_id = input("Enter your Spotify clientID ")
client_secret = input("Enter your Spotify secret client key ")

while(True):
    vidID = input("Enter your YouTube videoID ")

    # Create YT connection
    youtube = build('youtube', 'v3',
        developerKey=googleAPIkey)
    # Create Spotify connection
    app_token = tk.request_client_token(client_id, client_secret)
    spotify = tk.Spotify(app_token)

    redirect_uri = 'https://example.com/callback'

    user_token = tk.prompt_for_user_token(
        client_id,
        client_secret,
        redirect_uri,
        scope=tk.scope.playlist_modify_private
    )
    spotify.token = user_token
    userid = spotify.current_user().id

    def getYTdata(vidID):
        request = youtube.videos().list(id=vidID, part='snippet').execute()
        if request["items"]:
            desc = request["items"][0]['snippet']['description']
            name = request["items"][0]['snippet']['title']
            songs = re.findall(r'\[(?:\d+:)?\d+:\d+\]\s+(.*)\s+-\s+(.*)', desc)
            return (name, songs)
        else:
            raise Exception("Invalid video ID. Video not found.")

    # Create playlist
    def makePlaylist(name, songs):
        playlist = spotify.playlist_create(userid, name, public=False, description='')
        songuris = []
        for artist, song in songs:
            result = spotify.search(song + ' ' + artist, types=('track',))
            if result[0].items:
                songuris.append(result[0].items[0].uri)
            else:
                print('Song', artist, song, 'not found. Try manually searching with fewer keywords')
        spotify.playlist_add(playlist.id, songuris, position=None)


    name, songs = getYTdata(vidID)
    makePlaylist(name, songs)