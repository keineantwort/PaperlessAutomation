#!/bin/bash
curl -sL https://api.github.com/repos/keineantwort/PaperlessAutomation/tags \
  | jq -r '.[0].zipball_url' \
  | xargs -I {} curl -sL {} -o latest.zip

unzip -o latest.zip > /dev/null 2>&1

# find the directory
target_dir=$(find . -name "keineantwort-PaperlessAutomation-*" -type d)

# test if the directory is unzipped
if [ -z "$target_dir" ]; then
  echo "No directory with source starting with 'keineantwort-PaperlessAutomation-' found."
  exit 1
fi

# move everything to installation directory
mv "$target_dir"/* .

# delete installation files and unused directories
rm  -rf "$target_dir" latest.zip
chmod a+x post_consumption.sh

echo "Installation done. Find out how to configure at https://github.com/keineantwort/PaperlessAutomation/blob/main/Readme.md"