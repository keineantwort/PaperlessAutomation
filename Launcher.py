import asyncio
import importlib
import os

import yaml

from pla import PaperlessAccess


class Launcher:
    def __init__(self, config_file="launcher.yaml"):
        with open(config_file, 'r') as f:
            self._config = yaml.safe_load(f)
            self._rootdir = os.getcwd()

    def launch_post_consumption(self):
        paperless_access = PaperlessAccess(url=self._config["credentials"]["url"], token=self._config["credentials"]["api_token"])
        for module in self._config["postconsumption"]:
            print(f"launching {module}")
            path = os.path.join(self._rootdir, module)
            script = importlib.import_module(f".main", package=module)
            os.chdir(path)
            print(f"set working dir to {path}")
            asyncio.run(script.main(paperless_access))
            os.chdir(self._rootdir)
