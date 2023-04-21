# Youtube to Spotify
A Python utility that converts music compilation videos on YouTube into a Spotify playlist using Python, YouTube and Spotify API.

## Required libraries
* **googleapiclient**
* **tekore**

## Usage
* Lauch the program using `python YoutubeToSpotify.py` from a command line
* Input your GoogleAPI key. You can get one [here](https://developers.google.com/youtube/v3/getting-started).
* Input your Spotify client ID. You can get one [here](https://developer.spotify.com/documentation/general/guides/authorization/app-settings/)
* Input your Spotify secret client key. You can get it from the same link as above.
* Enter the ID of the Youtube video you want to convert. For example the ID of the following video `https://www.youtube.com/watch?v=QkKpbkpwv0U` is `QkKpbkpwv0U`
* You will be redirected to Spotify and asked to login.
* After logging in, please copy the URL you were redirected to and paste into the command line. A redirect URL looks like the following: `https://example.com/callback?code=LONG_STRING_OF_CHARACTERS`
* The application will now create a new Playlist in your Spotify with the title of the Youtube video you specified. You will be notified in the command line if a song cannot be found. After the program has finished you can enter another video ID to convert to a Spotify Playlist.
