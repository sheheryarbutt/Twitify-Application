import spotipy
import spotipy.util as util




# 'user-library-read'
scope ='playlist-modify-private'
username="SpotifyUsername"  # Put your own Spotify Username
playlist_name = 'Twitify for ' + username

token = util.prompt_for_user_token(username, scope, 'Client ID',
                                           'Client Secret', 'http://localhost:8888/callback')  # redirect URI
if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    playlists = sp.user_playlist_create(username, playlist_name, public=False)
    playlist_id = playlists['uri']
else:
    print("Can't get token for", username)


def get_valid_artist_id(artist_name):
    name=artist_name
    results = sp.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        if items[0]['followers']['total']>10000:
            return items[0]['name']


def add_artist_related_songs(artist_name):
    result = sp.search(q='artist:' + artist_name, type='artist')
    uri = result['artists']['items'][0]['uri']
    related = sp.artist_related_artists(uri)
    for i in range(0,5,2):
        response = sp.artist_top_tracks(related['artists'][i]['uri'])
        for j in range (0,2):
            sp.user_playlist_add_tracks(username, playlist_id, [response['tracks'][j]['uri']])
