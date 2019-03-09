# top-tracks
A lightweight playlist generator.

## How to use:

1. Install dependencies:

    ```
    python setup.py install
    ```

2. Generate Spotify API client id + secret here: https://developer.spotify.com/documentation/general/guides/authorization-guide/, and set the environment variables 'SPOTIFY_CLIENT_ID' and 'SPOTIFY_CLIENT_SECRET' in your local environment.

3. Generate top tracks from a set of artists:

    ```python top_tracks.py "Ariana Grande"```

    or

    ```python top_tracks.py -f coachella19.txt -o coachella19playlist.txt```

## Optional arguments:
A file with line separated artists, can be specified by ```-f```.

A file to output the playlist, can be specified by ```-o```.

Please check out `python top_tracks.py -h` for additional features and arguments.

## Playing the playlist:
Either use some fancy script to convert the playlist to a spotify/whatever-playlist, or simply play the raw playlist using e.g. https://github.com/kaada/please-play and the ```-f``` flag.
