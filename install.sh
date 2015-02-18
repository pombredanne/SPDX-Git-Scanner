#!/bin/bash
#Copyright © 2015 Daniel Patten, Zachary Meyer, and Jacob Vosik
#Setup User Name and Password for MySql
read -p "Enter your MySQL Username:" u
stty -echo 
 read -p "Enter your MySQL Password: " p; echo 
 stty echo
#Clone Repos
git clone https://github.com/socs-dev-env/SOCSDatabase

#Install Database
echo "Install SPDX Database..."
mysql --user=$u --password=$p < SOCSDatabase/SQL/SPDX.sql
#Exit mySql

#Delete Database Repo
echo "Remove Database Repo"
sudo rm SOCSDatabase -R
chmod 755 src/*.py
chmod 755 DoSOCS/src/*.py
echo "Install Complete"