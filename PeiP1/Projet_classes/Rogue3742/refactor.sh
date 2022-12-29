#!/bin/bash
echo "" > images2.py


IFS=$'\n'       # make newlines the only separator
set -f          # disable globbing
for i in $(cat "images.py" | grep "= {"); do
  echo "$i" >> images2.py
done
