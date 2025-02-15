import argparse
import os

from Launcher import Launcher

import asyncio

# shorthand for the class whose __del__ raises the exception
_BEL = asyncio.base_events.BaseEventLoop

_original_del = _BEL.__del__


def _patched_del(self):
    try:
        # invoke the original method...
        _original_del(self)
    except:
        # ... but ignore any exceptions it might raise
        # NOTE: horrible anti-pattern
        pass


# replace the original __del__ method
_BEL.__del__ = _patched_del

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Post consumption script for paperless ngx.')
    parser.add_argument('-d', '--document_id', type=int, help='the ID for the document to handle')
    parser.add_argument('-w', '--working_dir', type=str, help='the owrking dir for this script.', default=os.getcwd())
    args = parser.parse_args()

    print(f"Launching post consumption for {args.document_id} with configuration in {args.working_dir}.")

    launcher = Launcher(document_id=args.document_id, working_dir=args.working_dir)
    launcher.launch_post_consumption()
