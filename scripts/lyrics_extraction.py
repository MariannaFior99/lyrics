# import required packages
import json
import requests


def get_lyrics(artist, song):

    '''Get the lyrics with api.'''

    url = "https://api.lyrics.ovh/v1/" + artist + "/" + song
    # get the request from url
    response = requests.get(url)
    # store the response into change_lyrics
    change_lyrics = response.json()

    return change_lyrics["lyrics"]
