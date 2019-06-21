#!/bin/bash


mkdir datacore
mkdir public_backup

# set files in folders
mv backup_maker.py datacore
mv configure_requirements.sh datacore
mv core.py datacore
mv argv_system datacore
mv database.db datacore
mv Gitter.py datacore
mv Installer.py datacore
mv annimations_cgi.py datacore


cp ./datacore/database.db ./public_backup/  # for backup
./datacore/configure_requirements.sh  # execute requirements
rm -f ./installer.sh

