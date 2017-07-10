import time
import traceback

import yaml

from builders import MastodonBuilder, TwitterBuilder
from lastid import LastId
import settings


config = settings.FileConfiguration('config.yaml')


def check_new_tweets():
    twitter = TwitterBuilder(config).build()
    mastodon = MastodonBuilder(config).build()

    last_id_handler = LastId(config)
    last_id = last_id_handler.read()

    if last_id is not None:
        tweets = twitter.statuses.user_timeline(
            screen_name=config.TWITTER_ACCOUNT, since_id=last_id)
    else:
        tweets = twitter.statuses.user_timeline(
            screen_name=config.TWITTER_ACCOUNT)

    previous_last_id = last_id
    for tweet in reversed(tweets):
        print(tweet['text'])
        mastodon.toot(tweet['text'])
        last_id = tweet['id']

    if previous_last_id != last_id:
        print('New last Twitter status id is {}'.format(last_id))
        last_id_handler.write(last_id)

def main():
    while True:
        try:
            check_new_tweets()
        except:
            print(traceback.format_exc())

        time.sleep(60)

if __name__ == '__main__':
    main()
