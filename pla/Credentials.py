import yaml


class Credentials:
    def __init__(self, credentials_file):
        with open(credentials_file, 'r') as f:
            self._credentials = yaml.safe_load(f)

    def url(self):
        return self._credentials["url"]

    def token(self):
        return self._credentials["api_token"]