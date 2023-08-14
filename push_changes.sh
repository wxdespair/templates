#!/bin/bash

LOGFILE="./log/push_changes_log/logfile.log"

# cd /path/to/your/repo

echo "[>>> Start : $(date) <<<]" | tee -a $LOGFILE

git add . 2>&1 | tee -a $LOGFILE

git commit -m "Automated commit" 2>&1 | tee -a $LOGFILE

git push 2>&1 | tee -a $LOGFILE

echo "[>>> End : $(date) <<<]" | tee -a $LOGFILE
echo "" >> $LOGFILE
echo "" >> $LOGFILE

echo "Changes pushed and log saved to $LOGFILE"
