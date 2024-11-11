from pypaperless import Paperless

from pla.Credentials import Credentials


class PaperlessAccess:
    def __init__(self, credentials_file: str = "cred.yaml"):
        self._credentials = Credentials(credentials_file=credentials_file)
        print(f"Got credentials for {self._credentials.url()}")
        self._paperless_object = Paperless(url=self._credentials.url(), token=self._credentials.token(), request_args={"ssl": False})

    def paperless(self):
        if not self._paperless_object:
            raise Exception("no paperless instance could be found. Please initilize PaperlessAccess properly.")

        return self._paperless_object
