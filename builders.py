from twitter import Twitter, OAuth
from mastodon import Mastodon


class ConfigBasedBuilder:
    def __init__(self, config):
        self.config = config


class MastodonBuilder(ConfigBasedBuilder):
    def build(self):
        return Mastodon(
            client_id=self.config.MASTODON_CLIENTCRED_FILE,
            access_token=self.config.MASTODON_USERCRED_FILE,
            api_base_url=self.config.MASTODON_BASE_URL)


class TwitterBuilder(ConfigBasedBuilder):
    def build(self):
        auth = OAuth(
            self.config.TWITTER_TOKEN,
            self.config.TWITTER_TOKEN_SECRET,
            self.config.TWITTER_API_KEY,
            self.config.TWITTER_API_SECRET)
        return Twitter(auth=auth)
