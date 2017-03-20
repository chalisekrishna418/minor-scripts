import os, re

def get_essentials():
	user = raw_input("Enter Username for sftp user: ")
	add_groups = raw_input("Enter group if you want to add "+ user+" to other groups than www-data: ")
	bind_location = raw_input("Enter the location to be binded with /home/"+user+": ")
	public_key = raw_input("Enter the public key: ")
	return user, add_groups, bind_location, public_key
	
def create_user(user):
	command = "useradd -G www-data " + user
	os.system(command)
	command1 = "mkdir -p /home/" + user
	os.system(command1)
	command2 = "usermod -d /home/" + user +"/ " +user
	os.system(command2)
	print "user created"
	
def add_to_group(user, group):
	command = "usermod -a -G "+ group +" " + user
	os.system(command)
	print "user added to " + group + " group"
	
def give_sftp(user, group, key):
	command = "mkdir /home/"+user+"/.ssh/"
	os.system(command)
	file_location = "/home/"+user+"/.ssh/authorized_keys"
	f = open(file_location,"a") #opens file with name of "test.txt"
	f.write(key)
	f.write("\n")
	f.close()
	print "key file added"
	
def configure_permission(user):
	command = "chown -R root:root /home/"+user
	os.system(command)
	command1 = "chmod 755 /home/" + user
	os.system(command1)
	command2 = "mkdir -p /home/"+user+"/public_html"
	os.system(command2)
	loc = "/home/" + user + "/public_html"
	command3 = "chown -R " + user +":"+ user + " " + loc
	os.system(command3)
	print "permission managed for sftp"
	
def bind_user_loc(user, loc):
	command = "mount --bind "+ loc + " /home/"+user+"/public_html"
	os.system(command)
	print "drive mounted for sftp usage"
	
def end_msg():
	print "The process completed successfully"

def main():
	user, add_groups, bind_location, key = get_essentials()
	create_user(user)
	add_to_group(user, add_groups)
	give_sftp(user, add_groups, key)
	configure_permission(user)
	bind_user_loc(user, bind_location)
	
if __name__ == '__main__':
    main()

