#!/bin/bash

#script to be run at the mediator PC

#required credentials

#for source_server

source_server_key_loc="/home/krishna/Desktop/keys/draft.pem"
source_server_user="centos"
source_server_hostname="wp.draftserver.com"

#for client_server
client_server_key_loc=""
client_server_user=""
client_server_hostname=""


command="ssh -i "$source_server_key_loc" "$source_server_user"@"$source_server_hostname" 'bash -s' < ./migration.sh"
echo $command
$command
