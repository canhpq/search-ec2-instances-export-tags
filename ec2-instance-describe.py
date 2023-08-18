#Instance Id
import boto3
client = boto3.client('ec2')
Myec2=client.describe_instances()
for pythonins in Myec2['Reservations']:
 for printout in pythonins['Instances']:
  print(printout['InstanceId'])
 
# #Instance Type
# import boto3
# client = boto3.client('ec2')
# Myec2=client.describe_instances()
# for pythonins in Myec2['Reservations']:
#  for printout in pythonins['Instances']:
#   print(printout['InstanceId'])
#   print(printout['InstanceType'])