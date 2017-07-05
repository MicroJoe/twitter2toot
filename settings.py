import yaml


class DefaultConfiguration:
    # Mastodon

    MASTODON_APP_NAME = 'twitter2toot'

    MASTODON_BASE_URL = 'https://mastodon.social'
    MASTODON_USER_EMAIL = 'example@example.com'

    MASTODON_CLIENTCRED_FILE = 'pytooter_clientcred.secret'
    MASTODON_USERCRED_FILE = 'pytooter_usercred.secret'

    # Twitter

    TWITTER_ACCOUNT = 'twitter'
    TWITTER_LASTID_FILE = 'twitter_last_id.txt'

    TWITTER_API_KEY = 'not_a_chance'
    TWITTER_API_SECRET = 'not_a_chance'

    TWITTER_TOKEN = 'not_a_chance'
    TWITTER_TOKEN_SECRET = 'not_a_chance'


class FileConfiguration:
    def __init__(self, yaml_file):
        self.default = DefaultConfiguration()
        with open(yaml_file) as f:
            self.custom = yaml.load(f)

    def __getattr__(self, attr):
        try:
            return self.custom[attr]
        except KeyError:
            return getattr(self.default, attr)
