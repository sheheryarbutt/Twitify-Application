import time
import sys
import spotipy
import spotipy.util as util
import tweepy
import pprint
import os
from TwitterSetup import find_following
from SpotifySetup import get_valid_artist_id,add_artist_related_songs



if __name__== "__main__":

    following_list=find_following("TwitterUsername") #Put your own Twitter Username
    valid_artists = []
    for i in range(0, len(following_list)):
        if(get_valid_artist_id(following_list[i]) != None):
            valid_artists.append(get_valid_artist_id(following_list[i]))
    for j in range(0, len(valid_artists) - 1):
        add_artist_related_songs(valid_artists[j])