#!/bin/bash

# Set your paths below. Script can be run from any folder as long as your the right user and the drive is mounted.
# You can either include or exclude the database, incase you have mysql or simply don't want to backup a big file.

BACKUP_FOLDER=/mnt/wd_ext_hdd_2/hass_backup/
BACKUP_FILE=${BACKUP_FOLDER}hass-config_$(date +"%Y%m%d_%H%M%S").zip
BACKUP_LOCATION=/home/homeassistant/.homeassistant
INCLUDE_DB=false
DAYSTOKEEP=1 # Set to 0 to keep it forever.
LOGFILE=/var/log/backup-logs/home-assistant-backup.log

log() {
        if [ "${DEBUG}" == "true" ] || [ "${1}" != "d" ]; then
                echo "[${1}] ${2}"
                if [ "${3}" != "" ]; then
                        exit ${3}
                fi
        fi
}

if [ -d "${BACKUP_FOLDER}" ]; then
        if [ ! -d "${BACKUP_LOCATION}" ]; then
                log e "Homeassistant folder not found, is it correct?" 1
        fi
        pushd ${BACKUP_LOCATION} >/dev/null
        if [ "${INCLUDE_DB}" = true ] ; then
                log i "Creating backup with database"
                zip -9 -q -r ${BACKUP_FILE} . -x"components/*" -x"deps/*" -x"home-assistant.log"
        else
                log i "Creating backup"
                zip -9 -q -r ${BACKUP_FILE} . -x"components/*" -x"deps/*" -x"home-assistant.db" -x"home-assistant_v2.db" -x"home-assistant.log"
        fi

        popd >/dev/null

        log i "Backup complete: ${BACKUP_FILE}"
        if [ "${DAYSTOKEEP}" = 0 ] ; then
                log i "Keeping all files no prunning set"
        else
                log i "Deleting backups older then ${DAYSTOKEEP} day(s)"
                OLDFILES=$(find ${BACKUP_FOLDER} -mindepth 1 -mtime +${DAYSTOKEEP} -delete -print)
                if [ ! -z "${OLDFILES}" ] ; then
                        log i "Found the following old files:"
                        echo "${OLDFILES}"
                fi
        fi
else
        log e "Backup folder not found, is your USB drive mounted?" 1
fi
