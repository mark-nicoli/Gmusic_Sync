import sys
from gmusicapi import Mobileclient

api = Mobileclient()

api.perform_oauth()

library = api.get_all_songs()
sweet_track_ids = [track['id'] for track in library if track['artist'] == 'the cat empire']

playlist_id = api.create_playlist('rad muzik')

api.add_songs_to_playlist(playlist_id, sweet_track_ids)
