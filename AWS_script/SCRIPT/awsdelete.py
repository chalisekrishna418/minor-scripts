import boto3
import collections
import datetime

ec = boto3.client('ec2')
today = datetime.date.today().strftime('%Y-%m-%d')
data = 2
validity = 20

def lambda_handler(event, context):
    delete(event, context)
    
    #defining some variables
    snap_name = ""
    snap_id = ""
    
    #list for VolumeId adn Instance name
    ins_list1=[]
    
    #variable for loop counting
    count=0
    
    #selects instances that are to be backed up
    reservations = ec.describe_instances(
        Filters=[
            {'Name': 'tag-key', 'Values': ['backup', 'Backup']},
        ]
    ).get(
        'Reservations', []
    )

    instances = sum(
        [
            [i for i in r['Instances']]
            for r in reservations
        ], [])
    
	#print no. of instances to be backed up
    print "Found %d instances that need backing up" % len(instances)
    
    #prepare a delete_fmt for deletion date in a standard format
    delete_date = datetime.date.today() + datetime.timedelta(days=validity)
    delete_fmt = delete_date.strftime('%Y-%m-%d')
    
    #this for loop is for recording the volumeid and instance names
    #the even position consists of volumeId
    #the odd positions consists of Instance names
    for instance in instances:
    	tags = instance['Tags']
    	for dev in instance['BlockDeviceMappings']:
            if dev.get('Ebs', None) is None:
                continue
            vol_id = dev['Ebs']['VolumeId']
        ins_list1.append(vol_id)
        for tag in tags:
			if(tag['Key']=="Name"):
				ins_name = tag['Value']
				#ins_list[count-1][0]=ins_name
				ins_list1.append(ins_name)
			print "a"
        print "b"
    print "b"
    
	#the total length of list of instances to be backed up- only for debugging
    #its value needs to be twice the no. of instances to be backed up
    print len(ins_list1)
    
    #this loop is to create snapshot and tag those snapshots providing 
    #them with their names and expiry date
    #the volumeId and instance names are retreived from the ins_list1 list
    for i,ins in enumerate(ins_list1):
	    print ins
	    if(i%2==0):
	        print ins
	        print "hello"
	        snap_id = ec.create_snapshot(
			    VolumeId= ins,
		    )
	    if(i%2!=0):
	        snap_name = ins + " " + today
            print snap_name
            ec.create_tags(
                Resources=[snap_id['SnapshotId']],
                Tags=[
                    {'Key': 'DeleteOn', 'Value': delete_fmt},
                    {'Key': 'Name', 'Value': snap_name},
                ]
            )
	    print snap_id
	    
#the method to delete older snapshots which has crossed its expiry date
def delete(event, context):
    print "deleting.."
    
    #getting present date
    today1 = datetime.date.today().strftime('%Y-%m-%d')
    today = datetime.datetime.strptime(today1, '%Y-%m-%d')
    
    
    snapshot_response = ec.describe_snapshots(
         Filters=[
            {'Name': 'tag-key', 'Values': ['DeleteOn']},
        ])
        
    for snap in snapshot_response['Snapshots']:
        for i in snap['Tags']:
            key = i['Key']
            if(key == "DeleteOn"):
                expiry_date1 = i['Value']
                expiry_date = datetime.datetime.strptime(expiry_date1, '%Y-%m-%d')
                delta = today - expiry_date
                print delta.days
                if(delta.days == 0):
                    print "to be deleted"
                    print "Deleting snapshot %s" % key
                    ec.delete_snapshot(SnapshotId=snap['SnapshotId'])
