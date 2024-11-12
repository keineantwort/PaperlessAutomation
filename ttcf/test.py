import asyncio

import yaml

from pla import PaperlessAccess
from ttcf.main import main

if __name__ == '__main__':
    with open("../cred.yaml", 'r') as f:
        _config = yaml.safe_load(f)
        paperless_access = PaperlessAccess(url=_config["url"], token=_config["api_token"])
        asyncio.run(main(paperless_access))
