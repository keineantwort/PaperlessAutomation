#!/bin/bash
curl -sL https://api.github.com/repos/keineantwort/PaperlessAutomation/tags \
  | jq -r '.[0].zipball_url' \
  | xargs -I {} curl -sL {} -o latest.zip

unzip -o latest.zip

# find the directory
target_dir=$(find . -name "keineantwort-PaperlessAutomation-*" -type d)

# test if the directory is unzipped
if [ -z "$target_dir" ]; then
  printf "No directory with source starting with 'keineantwort-PaperlessAutomation-' found."
  exit 1
fi
ls -al
# move everything to installation directory
cp "$target_dir"/*.yaml_example .
mkdir pa
mv "$target_dir"/* pa

# delete installation files and unused directories
#rm  -rf "$target_dir" latest.zip
chmod a+x pa/post_consumption.sh

source .venv/bin/activate
pip install -r pa/requirements.txt

printf "\n\n ********************************** INSTALLATION DONE **********************************\n\n"
printf "Installation done. Find out how to configure at https://github.com/keineantwort/PaperlessAutomation/blob/main/Readme.md"