#!/bin/python

import re, sys
import os

ss_script_file="/home/krishna/scripts/site-migration/server.sh"
cs_script_file="/home/krishna/scripts/site-migration/client.sh"
finalize_script_file="/home/krishna/scripts/site-migration/finalize.sh"

def get_source_essentials():
	source_server_key_loc=raw_input("Enter the source server keyfile location: ")
	source_server_user=raw_input("Enter the source server username: ")
	source_server_hostname=raw_input("Enter the source server hostname: ")
	return source_server_key_loc, source_server_user, source_server_hostname

def get_client_essentials():
	client_server_key_loc=raw_input("Enter the client server keyfile location: ")
	client_server_user=raw_input("Enter the client server username: ")
	client_server_hostname=raw_input("Enter the client server hostname: ")
	return cskl, csu, csh

def create_ssh_command(skl, su, sh, script_file):
	command = "ssh -i " + skl + " " + su + "@" + sh + " 'bash -s' < "+ script_file
	print command
	return command

def ask_for_download():
	choice = raw_input("Do you want to download the files to your PC (y/n): ");
	if(choice == "y"):
		return true
	if(choice == "n"):
		return false
	else:
		print ("Invalid Input!!! \n Please Enter (y/n): ")
		ask_for_download()

def download_files(url, files)
	command = "wget " + url + " project." + files
	os.system("")

def execute_command(command):
	os.system(command)

def main():
	sskl, ssu, ssh = get_source_essentials()
	cskl, csu, csh = get_client_essentials()
	ss_command = create_ssh_command(sskl, ssu, ssh, ss_script_file)
	execute_command(ss_command)
	cs_command = create_ssh_command(cskl, csu, csh, cs_script_file)
	execute_command(cs_command)

	choice = ask_for_download()
	final_command = create_ssh_command(cskl, csu, csh, finalize_script_file)
	execute_command(final_command)

if __name__ == '__main__':
     main()

