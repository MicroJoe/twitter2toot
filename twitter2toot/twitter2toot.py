import sys
import time
import traceback

from twitter2toot.builders import MastodonBuilder, TwitterBuilder
from twitter2toot.lastid import LastId

from twitter2toot import settings


def check_new_tweets(config):
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


def main(config_file):
    config = settings.FileConfiguration(config_file)

    while True:
        try:
            check_new_tweets(config)
        except:
            print(traceback.format_exc())

        time.sleep(60)


def usage():
    print("usage: twitter2toot <config.yaml>")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    main(sys.argv[1])
