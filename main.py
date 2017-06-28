import time

from builders import MastodonBuilder, TwitterBuilder
from lastid import LastId
import settings


def check_new_tweets():
    twitter = TwitterBuilder.build()
    mastodon = MastodonBuilder.build()

    last_id = LastId.read()

    if last_id is not None:
        tweets = twitter.statuses.user_timeline(
            screen_name=settings.TWITTER_ACCOUNT, since_id=last_id)
    else:
        tweets = twitter.statuses.user_timeline(
            screen_name=settings.TWITTER_ACCOUNT)

    previous_last_id = last_id
    for tweet in reversed(tweets):
        print(tweet['text'])
        mastodon.toot(tweet['text'])
        last_id = tweet['id']

    if previous_last_id != last_id:
        print('New last Twitter status id is {}'.format(last_id))
        LastId.write(last_id)

def main():
    while True:
        check_new_tweets()
        time.sleep(60)