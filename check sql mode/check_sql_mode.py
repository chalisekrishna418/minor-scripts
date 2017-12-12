#!/bin/python
import os,sys
import re	

def check_mode():
	command = "mysql -e 'SELECT @@GLOBAL.sql_mode' > sql_mode"
	output = os.system(command)
	print output

def read_file():
	file = open('sql_mode','r')

	for i,line in enumerate(file):
		if(i >= 1):
			print line
			if (line != "\0"):
				change_sql_mode()
	file.close()

def change_sql_mode():
	command = "mysql -e \"SET @@GLOBAL.sql_mode=''\""
	output = os.system(command)
	status = "changed"
	print "your SQL mode is changed"

def main():
	check_mode()
	read_file()

if __name__ == '__main__':
    main()