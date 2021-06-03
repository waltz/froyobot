# Froyo Bot

This bot generates a message from the Yogurt Commercial corpus and tweets it out.

## Usage

1. Install the super secret data files in to `resources/`.
2. Fetch the project dependencies: `$ pipenv install`
3. Get hot gibberish: `$ pipenv run python main.py`

## Testing

To run the unit tests do `$ python -m unittest discover tests` from the base project directory.

## Deployment

This is mean to be run as a Twitter App. You'll have to go out and register a
new application through the Twitter developer portal. Once your app is approved
you will get a key and secret, add those to the `.env` file as the
`CONSUMER_KEY` and `CONSUMER_SECRET`.

Once those keys are present, you'll need to authorize this app to tweet through
a bot account. Authorize this app by running `$ python froyobot/get_twitter_oauth_tokens.py`.
That script will output the `TOKEN` and `TOKEN_SECRET` credentials; copy these
and put them in the `.env` file or add them as environment variables.

## Toot

To actually publish a message to the bot account, run `$ python tweet.py`.
This will generate a new message from the seed data and will publish that
message as a new tweet on the linked account.
