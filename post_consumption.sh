#!/bin/bash
echo "paperless postconsumption for $DOCUMENT_ID"
python3 main.py --document_id $DOCUMENT_ID --config_file launcher.yaml