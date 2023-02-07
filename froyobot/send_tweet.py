import os

from twitter import *
from mastodon import Mastodon
from dotenv import load_dotenv

from .message_getter import MessageGetter

load_dotenv()

def getStatus():
    return MessageGetter(os.path.dirname(__file__) + '/../resources/data/nimrod').shuffle()

def postToTwitter(status):
    token = os.getenv('TOKEN')
    token_secret = os.getenv('TOKEN_SECRET')
    consumer_key = os.getenv('CONSUMER_KEY')
    consumer_secret = os.getenv('CONSUMER_SECRET')

    client = Twitter(auth=OAuth(token, token_secret, consumer_key, consumer_secret))
    response = client.statuses.update(status=getStatus())

    print('https://twitter.com/i/status/' + str(response['id']))

def postToMastodon(status):
    api_base_url = os.getenv('MASTODON_API_BASE_URL')
    access_token = os.getenv('MASTODON_ACCESS_TOKEN')

    client = Mastodon(
        api_base_url = api_base_url,
        access_token = access_token,
    )
    bots_response = client.toot(status)
    print(bots_response['uri'])

def sendTweet():
    status = getStatus()
    print(status)

    try:
        postToTwitter(status)
    except Exception as error:
        print("Posting to Twitter failed")
        print(error)

    try:
        postToMastodon(status)
    except Exception as error:
        print("Posting to Mastodon failed")
        print(error)

if __name__ == "__main__":
    sendTweet()
