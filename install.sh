#!/bin/bash
# SPDXLicenseID: Apache-2.0
#Copyright © 2015 Daniel Patten, Zachary Meyer, and Jacob Vosik
#Setup User Name and Password for MySql
read -p "Enter your MySQL Username: " u
stty -echo 
read -p "Enter your MySQL Password: " p; echo 
stty echo

read -p "Enter your Git Global Username (Enter to skip): " guser
read -p "Enter your Git Global Email (Enter to skip): " gemail

#Clone Repos
git clone https://github.com/SPDX-Git/SPDX-Git-Scanner
git clone https://github.com/socs-dev-env/SOCSDatabase
git clone https://github.com/socs-dev-env/DoSOCS

#Install Database
echo "Install SPDX Database..."
mysql --user=$u --password=$p < SOCSDatabase/src/1.2/SPDX.sql
#Exit mySql

#Setup Git Globals (Optional)
if [[ $guser = *[!\ ]* ]]; then
git config --global user.name $guser
fi
if [[ $gemail = *[!\ ]* ]]; then
git config --global user.email $gemail
fi

#Setup config for the user
sed -i 's/root/'$u'/g' SPDX-Git-Scanner/src/config.txt
sed -i 's/1234/'$p'/g' SPDX-Git-Scanner/src/config.txt

#Delete Database Repo and setup files
echo "Setting up files..."
cp -r DoSOCS/src/*.* SPDX-Git-Scanner/src
chmod 755 SPDX-Git-Scanner/src/*.py
sudo rm DoSOCS -R
sudo rm SOCSDatabase -R
echo "Install Complete"
