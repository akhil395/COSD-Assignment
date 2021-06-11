# 6. Script or Jenkins job to change EBS volumes from GP2 to GP3 ( Feel free to choose IOPS on GP3 or make it a parameter)

import boto3

ebs = boto3.client('ec2', region_name='us-east-2')

# Function to change EBS type to GP3 with volume ID & IOPS as parameter
def change_ebs_type(volumeid, iops):
    response = ebs.modify_volume(
        VolumeId=volumeid,
        VolumeType='gp3',
        Iops=iops,
    )
    print("EBS volume with id: {} changed to GP3 with IOPS : {}".format(volumeid, iops))
    if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
        print("Successfully updated Volume Type to GP3")

# calling function to change ebs volume type to GP3
change_ebs_type('vol-07824f6bbfb87384f', 200)
