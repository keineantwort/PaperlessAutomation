import asyncio
import importlib
import os

import yaml

from pla import PaperlessAccess


class Launcher:
    def __init__(self, document_id: int, working_dir=os.getcwd()):
        with open(os.path.join(working_dir, "launcher.yaml"), 'r') as f:
            self._config = yaml.safe_load(f)
            self._scriptdir = os.getcwd()
            self._workingdir = working_dir
            self._document_id = document_id

    def launch_post_consumption(self):
        paperless_access = PaperlessAccess(url=self._config["credentials"]["url"], token=self._config["credentials"]["api_token"])
        for module in self._config["postconsumption"]:
            print(f"launching {module}")
            path = os.path.join(self._scriptdir, module)
            config_file = os.path.join(self._workingdir, f"{module}.yaml")
            script = importlib.import_module(f".main", package=module)
            os.chdir(path)
            print(f"set working dir to {path}")
            asyncio.run(script.main(paperless_access, self._document_id, config_file))
            os.chdir(self._scriptdir)
