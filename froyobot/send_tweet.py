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

    status = getStatus()

    client = Twitter(auth=OAuth(token, token_secret, consumer_key, consumer_secret))
    response = client.statuses.update(status=getStatus())

    print('Post success.')
    print(response['text'])
    print(response['created_at'])
    print('https://twitter.com/i/status/' + str(response['id']))

if __name__ == "__main__":
    sendTweet()
