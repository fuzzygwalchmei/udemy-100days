import requests
from bs4 import BeautifulSoup
import lxml
from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

SPOTIPY_CLIENT_ID = os.getenv('spotify_id')
SPOTIPY_CLIENT_SECRET = os.getenv('spotify_api')
SPOTIPY_REDIRECT_URI = "https://example.com" #= os.getenv('spotify_base')


def get_songs():
        
    songs_url='https://www.billboard.com/charts/hot-100/1978-03-19'

    resp = requests.get(url=songs_url)
    resp.raise_for_status()

    page = BeautifulSoup(resp.text, 'lxml')
    songs = page.find_all('span', class_='chart-element__information__song')
    artists = page.find_all('span', class_='chart-element__information__artist')

    song_names = [song.getText() for song in songs]
    artist_names = [artist.getText() for artist in artists]

    return list(zip(song_names, artist_names))


def connect_spotify():

    spot = SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, 
                        client_secret=SPOTIPY_CLIENT_SECRET,
                        redirect_uri=SPOTIPY_REDIRECT_URI,
                        scope='playlist-modify-private',
                        show_dialog=True,
                        cache_path='token.txt')

    sp = spotipy.Spotify(auth_manager=spot)
    return sp

def find_song(sp, songs):
    song_urls = []
    for song in songs:
        result = sp.search(f"{song[0]} year:1978", type='track')
        try:
            uri = result["tracks"]["items"][0]["uri"]
            song_urls.append(uri)
            print(f"Song: {song[0]} added to lists")
        except IndexError as e:
            print(f"Song: {song[0]} doesnt exist on Spotify")
    return song_urls


songs = get_songs()
sp = connect_spotify()
playlist = sp.user_playlist_create(user=sp.me()['id'], name = '1978-03-19', public=False)


playlists = sp.user_playlists(sp.me()['id'])

song_urls = find_song(sp, songs)


sp.user_playlist_add_tracks(user=sp.me()['id'], playlist_id=playlist['id'], tracks = song_urls)
    
# for each in playlists['items']:
#     print(each['id'])

