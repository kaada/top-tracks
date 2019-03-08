import sys
import argparse
import os

import pprint
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class PlaylistGenerator():

    def __init__(self):
        self.client_id = os.environ['SPOTIFY_CLIENT_ID']
        self.client_secret = os.environ['SPOTIFY_CLIENT_SECRET']

        self.client_credentials_manager = SpotifyClientCredentials(client_id=self.client_id, \
                                                                   client_secret=self.client_secret)
        self.sp = spotipy.Spotify(client_credentials_manager=self.client_credentials_manager)

    def top_tracks(self, artist_name):
        artist_data = self.sp.search(q='artist:' + artist_name, type='artist')
        artist_uri = artist_data['artists']['items'][0]['uri']
        results = self.sp.artist_top_tracks(artist_uri)

        songs = []

        for r in results['tracks']:
            r_artist = r['artists'][0]['name']
            r_song_name = r['name']
            songs.append(f'{r_artist} - {r_song_name}')

        return songs

    def artists_to_tracks(self, artists):
        songs = []

        for a in artists:
            tracks = self.top_tracks(a)
            songs.extend(tracks)

        return songs

    def generate_from_file(self, filename):
        with open(filename) as f:
            artists = f.readlines()
            artists = [a.strip() for a in artists]

        return self.artists_to_tracks(artists)

    def write_to_file(self, list_of_songs, filename):
        with open(f'{filename}', 'w') as f:
            for s in list_of_songs:
                f.write(f'{s}\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Returns top tracks for a given set of artists.')
    parser.add_argument('searchkey', nargs='*', metavar='string', type=str, help='name of artist')
    parser.add_argument('-f', '--file', metavar='string', type=str, help='file with list of artists')
    parser.add_argument('-o', '--outputfile', metavar='string', type=str, help='file name to output playlist')
    args = parser.parse_args()

    pg = PlaylistGenerator()

    if args.file:
        songs = pg.generate_from_file(args.file)
    else:
        artist = ' '.join(args.searchkey)
        songs = pg.top_tracks(artist)

    if args.outputfile:
        pg.write_to_file(songs, args.outputfile)
    else:
        print(songs)
