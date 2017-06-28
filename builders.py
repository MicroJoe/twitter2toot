from twitter import Twitter, OAuth
from mastodon import Mastodon

import settings


class MastodonBuilder:
    @staticmethod
    def build():
        return Mastodon(
            client_id=settings.MASTODON_CLIENTCRED_FILE,
            access_token=settings.MASTODON_USERCRED_FILE,
            api_base_url=settings.MASTODON_BASE_URL)


class TwitterBuilder:
    @staticmethod
    def build():
        auth = OAuth(
            settings.TWITTER_TOKEN,
            settings.TWITTER_TOKEN_SECRET,
            settings.TWITTER_API_KEY,
            settings.TWITTER_API_SECRET)
        return Twitter(auth=auth)