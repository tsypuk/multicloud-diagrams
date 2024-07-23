#!/bin/bash

# Define the files to exclude
exclude_files=("./docs/icons/jpg/redis.jpg" "./docs/icons/jpg/docker.jpg" "./docs/icons/jpg/github_code.jpg" "./docs/icons/jpg/git_repository.jpg")

# Create an array of all .jpg files
all_files=(./docs/icons/jpg/*.jpg)
# Get the list of modified files in the tmp/drawio directory
modified_files=$(git status --porcelain | grep 'tmp/drawio/' | awk '{print $2}')


# Check if there are any modified files
if [ -n "$modified_files" ]; then
  for file in $modified_files; do
    echo $file
    /Applications/draw.io.app/Contents/MacOS/draw.io -q 100 -x -f jpg -r -o docs/icons/jpg "$file"
    jpg_file=$(echo "$file" | sed 's/\.drawio$/.jpg/')
    filename=$(basename "$jpg_file")

    # Run mogrify on the include_files
    mogrify -resize 50% "docs/icons/jpg/$filename"
  done
else
  echo "No modified files in tmp/drawio to process."
fi
