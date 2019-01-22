import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pprint
import os

if len(sys.argv) > 1:
    search_str = sys.argv[1]
else:
    print('Please specify an artist')
    exit(0)

client_id = os.environ['SPOTIFY_CLIENT_ID']
client_secret = os.environ['SPOTIFY_CLIENT_SECRET']

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

artist_data = sp.search(q='artist:' + search_str, type='artist')
artist_uri = artist_data['artists']['items'][0]['uri']

results = sp.artist_top_tracks(artist_uri)
for r in results['tracks']:
    print(r['name'])
