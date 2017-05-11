import os, sys
import re, datetime

database = "admin"
backup_path = "/home/krishna/test/"

def create_dump(dumpfilename,db):
	dump_cmd = "mongodump -u admin -p admin123 -d " + database + " --out " + backup_path + dumpfilename
	output = os.system(dump_cmd)

def delete_old_dumps(date_today):
	for dump in os.listdir(backup_path):
		if(is_old_file(dump, date_today)):
			rm_cmd = "rm -rf " + backup_path + dump
			os.system(rm_cmd)

def is_old_file(dump, date_today):
	#print dump
	out = re.match(r'(.*)+(\d\d\d\d-\d\d-\d\d)', dump)
	print out.group(2)
	filedate = out.group(2)
	date_obj = datetime.datetime.strptime(filedate, '%Y-%m-%d')
	delta = date_obj - datetime.datetime.today()
	if(delta.days < -3):
		return True
	else:
		return False

def main():
	today = str(datetime.date.today())
	filename = database + "+" +today
	create_dump(filename, database)
	print "dump file created"
	delete_old_dumps(datetime.date.today())
	print "dump files filtered"


if __name__ == '__main__':
     main()

