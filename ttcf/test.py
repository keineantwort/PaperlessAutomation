import asyncio

import yaml

from pla import PaperlessAccess
from ttcf.main import main

if __name__ == '__main__':
    with open("../launcher.yaml", 'r') as f:
        _config = yaml.safe_load(f)
        paperless_access = PaperlessAccess(url=_config["credentials"]["url"], token=_config["credentials"]["api_token"])
        asyncio.run(main(paperless_access, 6120))
