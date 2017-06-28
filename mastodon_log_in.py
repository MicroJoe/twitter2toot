from mastodon import Mastodon
import settings


mastodon = Mastodon(
    client_id=settings.MASTODON_CLIENTCRED_FILE,
    api_base_url='https://social.svallee.fr'
)

user = settings.MASTODON_USER_EMAIL
password = input("Password for user {}: ".format(user))

mastodon.log_in(
    user, password,
    to_file=settings.MASTODON_USERCRED_FILE
)
