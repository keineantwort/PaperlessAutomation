import os

import yaml

from Launcher import Launcher

if __name__ == '__main__':
    config_file = "launcher.yaml"
    print(os.getcwd())
    with open(config_file, 'r') as f:
        _config = yaml.safe_load(f)
    launcher = Launcher(config_file="launcher.yaml")
    launcher.launch_post_consumption()