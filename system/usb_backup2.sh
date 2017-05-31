#!/bin/bash

# Set your paths below. Script can be run from any folder as long as your the right user and the drive is mounted.
# You can either include or exclude the database, incase you have mysql or simply don't want to backup a big file.

BACKUP_FOLDER=/mnt/wd_ext_hdd_2/hass_backup/
BACKUP_FILE=${BACKUP_FOLDER}hass-config_$(date +"%Y%m%d_%H%M%S").zip
BACKUP_LOCATION=/home/homeassistant/.homeassistantsre
INCLUDE_DB=false
DAYSTOKEEP=1 # Set to 0 to keep it forever.
LOGFILE=/var/log/backup-logs/home-assistant-backup.log
TIMESTAMP=`date +%Y/%m/%d_%H:%M:%S`

#log() {
#        if [ "${DEBUG}" == "true" ] || [ "${1}" != "d" ]; then
#                echo "[${1}] ${2}"
#                if [ "${3}" != "" ]; then
#                        exit ${3}
#                fi
#        fi
#}

if [ -d "${BACKUP_FOLDER}" ]
then
  if [ ! -d "${BACKUP_LOCATION}" ]
  then
  echo log e "Homeassistant folder not found, is it correct?"
  echo $TIMESTAMP "Home Assistat backup fail - directory" $BACKUP_LOCATION "not found" | sudo tee --append $LOGFILE
  else
  if [ "${INCLUDE_DB}" = true ]
  then
    echo "Creating backup with database"
    zip -9 -q -r ${BACKUP_FILE} . -x"components/*" -x"deps/*" -x"home-assistant.log"
  else
  echo "Creating backup"
  zip -9 -q -r ${BACKUP_FILE} . -x"components/*" -x"deps/*" -x"home-assistant.db" -x"home-assistant_v2.db" -x"home-assistant.log"
  echo "Backup complete: ${BACKUP_FILE}"

if [ "${DAYSTOKEEP}" = 0 ]
then
echo "Keeping all files no prunning set"
else
echo "Deleting backups older then ${DAYSTOKEEP} day(s)"
OLDFILES=$(find ${BACKUP_FOLDER} -mindepth 1 -mtime +${DAYSTOKEEP} -delete -print)

if [ ! -z "${OLDFILES}" ]
then
echo "Found the following old files:"
echo "${OLDFILES}"
else
echo "Backup folder not found, is your USB drive mounted?"
