import os,sys
import re

#loc="/home/eb-krishna/Desktop/test123"

loc = sys.argv[1]
print loc

loc_match=re.match(r'/home/eb-krishna/Desktop/(.*)',loc)

project_name=loc_match.group(1)
#team_name=loc_match.group(1)
team_name="test"
url="http://git.ebpearls.com/"+team_name+"/"+project_name+".git"
print url

out=re.match(r'http://git.ebpearls.com/(.*)/(.*).git',url)
group_name1= out.group(1)
project_name1=out.group(2)

username="krishna"
password="delluser418"
git_url="http://"+username+":"+password+"@git.ebpearls.com/"+ group_name1 + ("/") + project_name1 + ".git"

#os.system('pwd')

#os.system('cd test123')

os.system('pwd')

command="cd "+project_name1+" && git stash && git pull"
print git_url
os.system(command)
print command
