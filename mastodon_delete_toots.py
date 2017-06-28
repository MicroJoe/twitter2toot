from builders import MastodonBuilder


mastodon = MastodonBuilder.build()
myid = mastodon.account_verify_credentials()['id']

for toot in mastodon.account_statuses(myid):
    mastodon.status_delete(toot['id'])
