#! /bin/bash
# a="/tmp/premier_script_`date +%Y%m%d-%H-%M-%S`.log"
# ls -R ~ > $a
# ls -R /tmp >> $a

#!/usr/bin/env bash

PATH=$(/usr/bin/getconf PATH || /bin/kill $$)

PASS="123"

if [ ! -v "$1" ]; then
    echo "Try again 1,-)"
    exit 1
fi
echo "$1"
if test "$1" = "$PASS" 2>/dev/null  ; then
    echo "Well done you can validate the challenge with : $PASS"
else
    echo "Try again 2,-)"
fi

exit 0
