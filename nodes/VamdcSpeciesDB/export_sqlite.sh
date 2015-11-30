#!/bin/bash

#Uncomment the following if running as a cron job (with the CWD elsewhere)
#SCRIPT_PATH="/home/doronin/space/doronin/VAMDC/python/NodeSoftware/nodes/VamdcSpeciesDB"
#cd $SCRIPT_PATH

#Remove the old database copy
rm speciesdb.sqlite

#re-create the database structure using migrations
python manage.py migrate --database export export

#Fill in the database
python2 export/export_db.py
