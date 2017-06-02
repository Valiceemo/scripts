#!/bin/bash

FOLDER=/home/pi/scripts/system/source-vars
HASS_LOCATION=/home/homeassistant/.homeassistants
BACKUP_FOLDER=/mnt/wd_ext_hdd_2/hass_backup/
BACKUP_FILE=${BACKUP_FOLDER}hass-config_$(date +"%Y%m%d_%H%M%S").zip
LOGFILE=/var/log/backup-logs/home-assistant-backup.log
INCLUDE_DB=false
TIMESTAMP=`date +%Y/%m/%d_%H:%M:%S`
DAYSTOKEEP=0

if
[ -d "$FOLDER" ]
then
if [ ! -d $HASS_LOCATION ]
then
echo "Homeassistant folder not found, is it correct?"
echo $TIMESTAMP "-" "Home Assistant backup fail - directory" $HASS_LOCATION "not found" | sudo tee --append $LOGFILE
#exit
else
if
[ $INCLUDE_DB == true ]
then
echo "Creating backup with database..."
zip -9 -q -r ${BACKUP_FILE} $HASS_LOCATION -x"components/*" -x"deps/*" -x"home-assistant.log"
echo $TIMESTAMP "-" "Home assistant backup made including database" | sudo tee --append $LOGFILE
echo "Backup made at" $LOGFILE
else
echo "Creating backup without database..."
zip -9 -q -r ${BACKUP_FILE} $HASS_LOCATION -x"components/*" -x"deps/*" -x"home-assistant.db" -x"home-assistant_v2.db" -x"home-assistant.log"
echo $TIMESTAMP "-" "Home assistant backup made without database" | sudo tee --append $LOGFILE
echo "Backup made at" $LOGFILE
fi
fi
fi