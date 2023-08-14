#!/bin/bash

LOGFILE="./log/push_changes_log/logfile.log"

# cd /path/to/your/repo

echo "Script started at $(date)" | tee -a $LOGFILE

git add .

git commit -m "Automated commit"

git push 2>&1 | tee -a $LOGFILE

echo "Script ended at $(date)" | tee -a $LOGFILE

echo "Changes pushed and log saved to $LOGFILE"
