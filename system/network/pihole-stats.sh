#!/bin/bash
# Author: Richard Wallace aka Valiceemo Very basic script to read
# pi-hole API, and log to stats to file, logic being a lengthier
# storgae of basic data See https://pi-hole.net/ for the awesome
# project. Edit file path for log file if desired Can be run from
# CL, or via crontab

LOGDIR=/home/pi/logs
LOGFILE=$LOGDIR/pihole.log
TIMESTAMP=`date +%Y/%m/%d_%H:%M`

# for debug + testing
# RAW=`curl "http://localhost/admin/api.php?summary"| jq '.'`

DNS_TODAY=`curl --silent "http://localhost/admin/api.php?summary"| jq '.dns_queries_today'`
ADS_TODAY=`curl --silent "http://localhost/admin/api.php?summary"| jq '.ads_blocked_today'`
ADS_PERCENT=`curl --silent "http://localhost/admin/api.php?summary"| jq '.ads_percentage_today'`

if [ ! -d "$LOGDIR" ]
then
sudo mkdir $LOGDIR
fi

if [ ! -f "$LOGFILE" ]
then
sudo touch $LOGFILE
echo $TIMESTAMP "-" "Log file created" | sudo tee --append $LOGFILE
echo | sudo tee --append $LOGFILE
fi

echo | sudo tee --append $LOGFILE
echo $TIMESTAMP | sudo tee --append $LOGFILE
echo "DNS Queuries:" $DNS_TODAY | sudo tee --append $LOGFILE
echo "Ads Blocked:" $ADS_TODAY | sudo tee --append $LOGFILE
echo "Percentage Blocked:" $ADS_PERCENT | sudo tee --append $LOGFILE
