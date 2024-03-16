#!/bin/bash

MAIN_FOLDER='C:/Users/fionn.sherrard/Downloads/assets/zip_test'

for SUBFOLDER in "$MAIN_FOLDER"/*;do
  if [ -d "$SUBFOLDER" ]; then
    echo "Processing $SUBFOLDER"

    hython run_on_template.py "D:/Rebelway/Week_6/Asset_Migration_Tools.hip" "$SUBFOLDER"

  fi
done

