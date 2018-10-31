import os,datetime

user=""
group=""

def read_files():
	file = open('lists.txt','r')
	for i,line in enumerate(file):
			make_tar(line[0:-1]);
			
def make_tar(line):
	dirf = ("%s" %line)
	filename = dirf + "\ " + str(datetime.date.today())
	print "making tar of " + dirf
	command ="cd " + dirf + " && tar -zcvf ../" + filename + ".tar.gz . && mv ../" + filename + ".tar.gz . && cd .. "
	print(command)
	output = os.system(command)
	print(output)
	permission_cmd = "chown -R "+ user + ":" + group + " " + dirf
	output1= os.system(command)
	print "tarfile of " + dirf + "created"
	
def main():
	read_files()
	
if __name__ == '__main__':
    main()

