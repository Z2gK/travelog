#!/bin/sh
# This script logs location information using the termux-location command
# The date and user-provided description will be captured together in
# a json structure and appended to a log file location.log
# When used in the Android environment, location access needs to be enabled
# The description should be enclosed in quotes (") when supplied to this script

if [ $# -eq 0 ]; then
    echo "This script logs location information using the termux-location command."
    echo "Note that location access needs to be turned on."
    echo "This script takes only one argument, i.e. the description, which"
    echo "needs to be enclosed in quotes."
    exit
fi

# This file will be stored in the home directory by default
LOGFILENAME="location.log"

DATESTRING=`date`
DESCRIPTIONSTRING=$1
LOCATIONSTRING=`termux-location`

if [ -z "$LOCATIONSTRING" ]
then
    # In this case, the output from termux-location is empty
    # We log only the date and description
    echo "{" >> $HOME/$LOGFILENAME
    echo '  "date": "'${DATESTRING}'",' >> $HOME/$LOGFILENAME
    echo '  "description": "'${DESCRIPTIONSTRING}'"' >> $HOME/$LOGFILENAME
    echo "}" >> $HOME/$LOGFILENAME
else
    # It is necessary to put $LOCATIONSTRING in quotes to preserve newlines
    LOCATIONOUTPUTSTRING=`echo "$LOCATIONSTRING" | head -n 10`
    echo "$LOCATIONOUTPUTSTRING""," >> $HOME/$LOGFILENAME
    echo '  "date": "'${DATESTRING}'",' >> $HOME/$LOGFILENAME
    echo '  "description": "'${DESCRIPTIONSTRING}'"' >> $HOME/$LOGFILENAME
    echo "}" >> $HOME/$LOGFILENAME
fi
