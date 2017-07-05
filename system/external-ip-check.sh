#!/bin/bash

# Checks external IP and send a mail to root if updated


LastIP=$(tail -1 /var/log/external-ip.log| awk '{print $2}')
CurrentIP=$(curl -s https://api.ipify.org)

if [[ "$CurrentIP" != "$LastIP" ]]
then
date +"%Y-%m-%d: " | tr -d '\n' >> /var/log/external-ip.log
echo "$CurrentIP"  >> /var/log/external-ip.log
echo "`hostname` has a new external IP, $CurrentIP" | mail -s "`hostname` IP Address Updated" "$EMAIL"
fi
