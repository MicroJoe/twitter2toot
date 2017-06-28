import settings


class LastId:
    @staticmethod
    def read():
        try:
            with open(settings.TWITTER_LASTID_FILE) as f:
                return int(f.read().splitlines()[0])
        except (FileNotFoundError, ValueError):
            return None

    @staticmethod
    def write(id):
        with open(settings.TWITTER_LASTID_FILE, 'w') as f:
            f.write('{}\n'.format(id))

        assert(LastId.read() == id)
