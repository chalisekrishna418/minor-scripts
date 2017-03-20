#!/usr/bin/python

import os,sys
import re

#the argument passed to this script looks like:
#"/var/opt/gitlab/git-data/repositories/test/test123.git"

#takes command line argument 
loc = sys.argv[1]
print loc	#for debug only

#compare the pattern of argument to find out the project name and team name
loc_match=re.match(r'/var/opt/gitlab/git-data/repositories/(.*)/(.*).git',loc)

project_name=loc_match.group(2)
team_name=loc_match.group(1)

#construct a git url for use
url="http://git.ebpearls.com/"+team_name+"/"+project_name+".git"
print url	#for debug only

#get project name and group name from url
out=re.match(r'http://git.ebpearls.com/(.*)/(.*).git',url)
group_name1= out.group(1)
project_name1=out.group(2)

#the username and password to use for git operations
username="krishna"
password="delluser418"

#the final git url which is ready to use
git_url="http://"+username+":"+password+"@git.ebpearls.com/"+ group_name1 + ("/") + project_name1 + ".git"

os.system('pwd')	#gives current location in draft server (for debug only)

#check if the working copy of project already exists or not

#if it exists then perform pull operation
if(os.path.exists(project_name1)):
	command="cd "+project_name1+" && git stash && git pull"
	os.system(command)
	print command

#if it doesnot exists then perform clone operation
else:
	command="git clone " + git_url
	os.system(command)
	print command
