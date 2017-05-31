#!/bin/bash

#script to be run at the source server end

#credentials required

#become root user (if required)
sudo su

#root password (if required)
#root_password=""

#necessary details

file_location="/home/wp/public_html/yell/"
cd $file_location
pwd
whoami
tar -zcvf ../project.tar.gz .
mv ../project.tar.gz .

