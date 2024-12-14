import argparse
import os

import yaml

from Launcher import Launcher

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Post consumption script for paperless ngx.')
    parser.add_argument('-d', '--document_id', type=int, help='the ID for the document to handle')
    parser.add_argument('-f', '--config_file', type=str, help='the configuration file for this script.', default="launcher.yaml")
    args = parser.parse_args()

    print(f"Launching post consumption for {args.document_id} with configuration in {args.config_file}.")

    launcher = Launcher(document_id=args.document_id, config_file=args.config_file)
    launcher.launch_post_consumption()
