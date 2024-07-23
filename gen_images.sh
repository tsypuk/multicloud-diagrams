#!/bin/bash

# Get the list of modified files in the tmp/drawio directory
modified_files=$(git status --porcelain | grep '^ M tmp/drawio/' | awk '{print $2}')


# Check if there are any modified files
if [ -n "$modified_files" ]; then
  for file in $modified_files; do
    /Applications/draw.io.app/Contents/MacOS/draw.io -q 100 -x -f jpg -r -o docs/icons/jpg "$file"
  done
else
  echo "No modified files in tmp/drawio to process."
fi

# Run mogrify on the include_files
mogrify -resize 50% "${include_files[@]}"
