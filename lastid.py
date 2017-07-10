
class LastId:
    def __init__(self, config):
        self.config = config

    def read(self):
        try:
            with open(config.TWITTER_LASTID_FILE) as f:
                return int(f.read().splitlines()[0])
        except (FileNotFoundError, ValueError):
            return None

    def write(self, id):
        with open(config.TWITTER_LASTID_FILE, 'w') as f:
            f.write('{}\n'.format(id))

        assert(LastId.read() == id)
