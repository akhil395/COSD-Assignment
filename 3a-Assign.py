#3. Using CloudFormation, deploy a Lambda function that monitors ELB creation events and enables ELB access logging on the ELB if it is not already enabled

import boto3


client = boto3.client('elb', region_name='us-east-2')
elbv2 = boto3.client('elbv2', region_name='us-east-2')
def lambda_handler(event, context):
    if event and event['detail-type'] == 'AWS API Call via CloudTrail':
        event_state = event['LoadBalancerDescriptions']['state']
        elb = (response['LoadBalancerDescriptions'][0]['DNSName'])
        elb_name = event['LoadBalancerDescriptions']['LoadBalancerName']
        if event_state == 'SUCCEEDED':
            try:
                res = client.describe_load_balancer_attributes(LoadBalancerName=elb_name)
                if not (res['LoadBalancerAttributes']['AccessLog']['Enabled']):
                    res1 = client.modify_load_balancer_attributes(
                        LoadBalancerName=elb_name,
                        LoadBalancerAttributes={'AccessLog': {
                            'Enabled': True}})

                    if res1["ResponseMetadata"]["HTTPStatusCode"] == 200:
                        print("Successfully enabled access logs : ")

                    else:
                        print("Access log is already enabled")

            except:
                res2 = client.modify_load_balancer_attributes(
                    LoadBalancerArn=elb,
                    Attributes={
                        {
                            'Key': 'access_logs.s3.enabled',
                            'Value': True,
                        },
                    }
                )
                if res2["ResponseMetadata"]["HTTPStatusCode"] == 200:
                    print("Successfully enabled access logs : ")
