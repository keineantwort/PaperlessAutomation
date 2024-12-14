#!/bin/bash
echo "paperless postconsumption for $DOCUMENT_ID"
script_dir=$(dirname "$(readlink -f "$0")")
parent_dir=$(dirname "$script_dir")
source "$parent_dir"/.venv/bin/activate
python3 "$script_dir"/main.py --document_id "$DOCUMENT_ID" --working_dir "$parent_dir"