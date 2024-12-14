import argparse
import os

import yaml

from Launcher import Launcher

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Post consumption script for paperless ngx.')
    parser.add_argument('-d', '--document_id', type=int, help='the ID for the document to handle')
    parser.add_argument('-w', '--working_dir', type=str, help='the owrking dir for this script.', default=os.getcwd())
    args = parser.parse_args()

    print(f"Launching post consumption for {args.document_id} with configuration in {args.working_dir}.")

    launcher = Launcher(document_id=args.document_id, working_dir=args.working_dir)
    launcher.launch_post_consumption()
