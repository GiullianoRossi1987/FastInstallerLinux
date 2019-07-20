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
# configure requirements
sudo apt-get install snapd
sudo apt-get install git
sudo apt-get install python-sqlite3
sudo apt-get install python3-sqlite3
sudo apt-get install python3-pip
sudo apt-get install figlet
sudo pip3 install processbar
rm -f ./installer.sh

