#!/bin/bash
#Copyright © 2015 Daniel Patten, Zachary Meyer, and Jacob Vosik
#Setup User Name and Password for MySql
read -p "Enter your MySQL Username:" u
stty -echo 
read -p "Enter your MySQL Password: " p; echo 
stty echo
#Clone Repos
git clone https://github.com/SPDX-Git/SPDX-Git-Scanner
git clone https://github.com/socs-dev-env/SOCSDatabase
git clone https://github.com/socs-dev-env/DoSOCS

#Install Database
echo "Install SPDX Database..."
mysql --user=$u --password=$p < SOCSDatabase/SQL/SPDX.sql
#Exit mySql

#Delete Database Repo
echo "Setting up files..."
cp -r DoSOCS SPDX-Git-Scanner
chmod 755 SPDX-Git-Scanner/src/*.py
chmod 755 SPDX-Git-Scanner/DoSOCS/src/*.py
sudo rm DoSOCS -R
sudo rm SOCSDatabase -R
echo "Install Complete"
