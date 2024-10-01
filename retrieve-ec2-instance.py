import boto3

# Initialize EC2 client
ec2_client = boto3.client('ec2')

# The ENI ID you're looking for
eni_id = 'eni-0ca61a748707dba88'  # Replace with your ENI ID

# Describe the network interface to find which instance it's attached to
response = ec2_client.describe_network_interfaces(
    NetworkInterfaceIds=[eni_id]
)

# Extract and print instance information
network_interface = response['NetworkInterfaces'][0]
attachment = network_interface.get('Attachment', {})

# Check if the ENI is attached to an EC2 instance
if 'InstanceId' in attachment:
    instance_id = attachment['InstanceId']
    print(f"ENI {eni_id} is attached to EC2 instance: {instance_id}")
else:
    print(f"ENI {eni_id} is not attached to any EC2 instance.")