from twitter2toot.builders import MastodonBuilder

from twitter2toot.settings import FileConfiguration

config = FileConfiguration('config.yaml')
mastodon = MastodonBuilder(config).build()
myid = mastodon.account_verify_credentials()['id']

for toot in mastodon.account_statuses(myid):
    mastodon.status_delete(toot['id'])
