'''
    Copify: authorize users sends authorization request, 
    and allows for custom playlist creation
'''
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

class Copify():

    def __init__(self):
        # initiate authentication client object
        self.sp_client = self._authenticate()

    def _authenticate():
        '''Authenticates the client for user access:
            returns an established `sp` client object
        '''

        # load the client variables
        load_dotenv()

        client_id = os.getenv('APP_CLIENT_ID')

        spotify_app_client_secret = os.getenv("SPOTIFY_APP_CLIENT_SECRET")

        spotify_app_redirect = os.getenv("SPOTIFY_APP_REDIRECT_URI")


        user_sp_client = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                client_secret=spotify_app_client_secret,
                                                redirect_uri=spotify_app_redirect,
                                                scope=["user-library-read","playlist-modify-private"]
                                                ),requests_timeout=30)

        return user_sp_client
    
    