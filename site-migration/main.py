#!/bin/python

import re, sys
import os

ss_script_file="/home/krishna/scripts/site-migration/server.sh"
cs_script_file="/home/krishna/scripts/site-migration/client.sh"

def get_source_essentials():
	source_server_key_loc=raw_input("enter the source server keyfile location: ")
	source_server_user=raw_input("enter the source server username: ")
	source_server_hostname=raw_input("enter the source server hostname: ")
	return source_server_key_loc, source_server_user, source_server_hostname

def get_client_essentials():
	client_server_key_loc=raw_input("enter the client server keyfile location: ")
	client_server_user=raw_input("enter the client server username: ")
	client_server_hostname=raw_input("enter the client server hostname: ")
	return cskl, csu, csh

def create_ssh_command(sskl, ssu, ssh, ss_script_file):
	command = "ssh -i " + sskl + " " + ssu + "@" + ssh + " 'bash -s' < "+ ss_script_file
	print command
	return command

def execute_command(command):
	os.system(command)

def main():
	sskl, ssu, ssh = get_source_essentials()
	#cskl, csu, csh = get_client_essentials()
	command = create_ssh_command(sskl, ssu, ssh, ss_script_file)
	execute_command(command)

if __name__ == '__main__':
     main()

