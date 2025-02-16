import asyncio
import importlib
import os
from enum import Enum

import yaml

from pla import PaperlessAccess


class Mode(Enum):
    POST_CONSUMPTION = "postconsumption"
    MANUAL = "manual"


class Launcher:
    def __init__(self, document_id: int, working_dir=os.getcwd()):
        with open(os.path.join(working_dir, "launcher.yaml"), 'r') as f:
            self._config = yaml.safe_load(f)
            self._scriptdir = os.path.dirname(os.path.abspath(__file__))
            self._workingdir = working_dir
            self._document_id = document_id
            print(f"{self._workingdir} > {self._scriptdir}")

    def launch_post_consumption(self):
        self._launch(Mode.POST_CONSUMPTION)

    def launch_manual(self):
        self._launch(Mode.MANUAL)

    def _launch(self, mode: Mode):
        paperless_access = PaperlessAccess(url=self._config["credentials"]["url"], token=self._config["credentials"]["api_token"])
        for module in self._config[mode.value]:
            print(f"launching {module}")
            path = os.path.join(self._scriptdir, module)
            config_file = os.path.join(self._workingdir, f"{module}.yaml")
            script = importlib.import_module(f".main", package=module)
            os.chdir(path)
            print(f"set working dir to {path}")
            asyncio.run(script.main(paperless_access, self._document_id, config_file))
            os.chdir(self._scriptdir)
