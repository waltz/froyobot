import os

from twitter import *
from dotenv import load_dotenv

def attemptOauthDance():
    load_dotenv()

    consumer_key = os.getenv('CONSUMER_KEY')
    consumer_secret = os.getenv('CONSUMER_SECRET')

    oauth_token, oauth_secret_token = oauth_dance("froyobot", consumer_key, consumer_secret)

    print("OAuth Token:", oauth_token)
    print("OAuth Secret Token:", oauth_secret_token)

if __name__ == "__main__":
    attemptOauthDance()
