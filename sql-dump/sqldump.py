import os

#writes all the available database names to a file
def writeDatabases():
	#opens (creates a file if doesnot exists and opens) a file named dbList.txt in write mode
#	file = open('dbList.txt','w')

	#define the first command to be executed
	#this command writes the output of the command to the file dbList.txt
	#the output of command is the list of databases present on the system
	command= "mysql --host=192.168.0.140 -e 'show databases' >> dbList.txt"
	
	#closes the previously opened file dbList.txt
#	file.close('dblist.txt');

	#executes the command described by the command variable
	os.system(command)

#dumps every database on loop 
def getDBName():

	#opens the file dbList.txt in readonly mode
	#this file is supposed to contain the list of databases
	#a line is a database name except the very first line which is a dummy text that cannot be avoided
	file = open('dbList.txt','r')

	#loop to scan each line of the dbList.txt file for database names
	for i,line in enumerate(file):
		
		#reads the line with line nos greater than or equal to 1 i.e. from 2nd line
		if(i >= 1):
		
			#calls the dumpdb method for database dump of database name 
			#whose name is in same line pointed by the loop
			#passes the whole line except the last character which is \n
			dumpdb(line[0:-1]);

	file.close()

#dumps the database
def dumpdb(line):

	#the name of the dump file which is same as the name of original database
	#written in standard formatting 
	filename = ("%s.sql" %line)

	#building the command to be executed
	command = 'mysqldump --host=192.168.0.140 ' + line + ' > ' + '/home/krishna/Desktop/datadump/' + filename

	#for interactive dump so the user can see which databases are dumped
	print(command)           #for interactive dump

	#executes the command for sql dump
	os.system(command)

#the main function
#the script starts from here
def main():
	writeDatabases()
	getDBName()

#the if section is written so this file can be imported to the other python shell scripts
#only the methods listed in if section can be imported from other python shells
if __name__ == '__main__':
    main()

