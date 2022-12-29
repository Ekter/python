#!/bin/bash
folder="$1"
while [ ! -d "$folder" ]; do
    echo "Please enter a valid folder"
    read folder
done
echo "The folder $folder contains the following files:"
ls -l "$folder"
