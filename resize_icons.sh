#!/bin/bash

# Define the files to exclude
exclude_files=("./docs/icons/jpg/redis.jpg")

# Create an array of all .jpg files
all_files=(./docs/icons/jpg/*.jpg)

# Create an array to hold the files to process
include_files=()

# Loop through all files and add to include_files if not in exclude_files
for file in "${all_files[@]}"; do
    echo $file
    if [[ ! " ${exclude_files[@]} " =~ " ${file} " ]]; then
        include_files+=("$file")
    fi
done

# Run mogrify on the include_files
mogrify -resize 50% "${include_files[@]}"
