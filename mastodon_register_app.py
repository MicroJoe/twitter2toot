from mastodon import Mastodon
import settings


Mastodon.create_app(
    settings.MASTODON_APP_NAME,
    api_base_url=settings.MASTODON_BASE_URL,
    to_file=settings.MASTODON_CLIENTCRED_FILE
)
