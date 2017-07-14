from mastodon import Mastodon

from twitter2toot.settings import FileConfiguration

config = FileConfiguration('config.yaml')

Mastodon.create_app(
    config.MASTODON_APP_NAME,
    api_base_url=config.MASTODON_BASE_URL,
    to_file=config.MASTODON_CLIENTCRED_FILE
)
