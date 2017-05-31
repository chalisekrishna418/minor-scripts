#!/bin/bash

#script to be run at the source server end

#credentials required

#become root user (if required)
sudo su

#root password (if required)
#root_password=""

#necessary details

file_location="/home/wp/public_html/"
project_name=""
server_url=""
db_name=""
site_user=""


cd $file_location
pwd
wget $server_url"/project.tar.gz"
wget $server_url"/project.sql"
tar -xvf ../project.tar.gz .
rm -f project.tar.gz
mysql $db_name < project.sql
rm -f project.sql
chown -R $site_user":"$site-user" ../"$project_name
