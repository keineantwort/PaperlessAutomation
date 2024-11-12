from pypaperless import Paperless


class PaperlessAccess:
    def __init__(self, url: str, token: str):
        print(f"Got credentials for {url}")
        self._paperless_object = Paperless(url=url, token=token, request_args={"ssl": False})

    def paperless(self):
        if not self._paperless_object:
            raise Exception("no paperless instance could be found. Please initilize PaperlessAccess properly.")

        return self._paperless_object
