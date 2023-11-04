#!/bin/bash

# Define the container name and directory
CONTAINER_NAME="b701e387dd4d"
CONTAINER_DIR="/bd-a1/"
LOCAL_DIR="bd-a1/service-result/"

# Array of files to copy
files=("dpre-out.txt" "eda-in-1.txt" "eda-in-2.txt" "eda-in-3.txt" "vis.png" "k.txt")

# Loop through the array and copy files
for file in "${files[@]}"
do
    docker cp "$CONTAINER_NAME:$CONTAINER_DIR$file" "$LOCAL_DIR$file"
done

# Stop the container
docker stop "$CONTAINER_NAME"
