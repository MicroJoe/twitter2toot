from mastodon import Mastodon

from twitter2toot.settings import FileConfiguration

config = FileConfiguration('config.yaml')

mastodon = Mastodon(
    client_id=config.MASTODON_CLIENTCRED_FILE,
    api_base_url='https://social.svallee.fr'
)

user = config.MASTODON_USER_EMAIL
password = input("Password for user {}: ".format(user))

mastodon.log_in(
    user, password,
    to_file=config.MASTODON_USERCRED_FILE
)
