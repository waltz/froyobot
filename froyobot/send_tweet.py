import os

from twitter import *
from dotenv import load_dotenv

from .message_getter import MessageGetter

def getStatus():
    return MessageGetter(os.path.dirname(__file__) + '/../resources/data/nimrod').shuffle()

def sendTweet():
    load_dotenv()

    token = os.getenv('TOKEN')
    token_secret = os.getenv('TOKEN_SECRET')
    consumer_key = os.getenv('CONSUMER_KEY')
    consumer_secret = os.getenv('CONSUMER_SECRET')

    client = Twitter(auth=OAuth(token, token_secret, consumer_key, consumer_secret))
    client.statuses.update(status=getStatus())

if __name__ == "__main__":
    sendTweet()
