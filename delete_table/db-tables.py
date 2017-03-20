import os,sys

db_name = raw_input("Enter Database name: ")

def create_db_list(database):
	query = "show tables in " + database
	command = "mysql -e \'" +query + "\' >> tablelists.txt"
	print query
	print command
	os.system(command)
	
def delete_tables(database):
	file = open('tablelists.txt','r')

	for i,line in enumerate(file):
		if(i >= 1):
		
			delete_table(database, line[0:-1]);

	file.close()

def delete_table(database, table_name):
	dbformat = database + "." + table_name
	print dbformat
	query = "drop table " + dbformat
	print "Deleting table " + dbformat
	command = "mysql -e \'" + query + "\'"
	os.system(command)
	
def main():
	create_db_list(db_name)
	delete_tables(db_name)
	
if __name__ == '__main__':
    main()
