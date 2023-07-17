import boto3
from datetime import datetime, timedelta
import pandas as pd
session = boto3.Session(profile_name = "xxxxxx", region_name = 'ap-southeast-1')
# Initialize the boto3 client
client = boto3.client('ec2')

# Get a list of all regions
regions = [region['RegionName'] for region in client.describe_regions()['Regions']]

# Initialize the NAT Gateway list
nat_gateways = []

# Loop through each region
for region in regions:
    # Create an EC2 client for the region
    ec2 = boto3.resource('ec2', region_name=region)
    
    # Get all NAT Gateways
    for nat_gateway in client.describe_nat_gateways()['NatGateways']:
        # Skip any NAT Gateways that are not in the current region
        if nat_gateway['Region'] != region:
            continue
        
        # Get the VPC and Subnet information
        vpc = ec2.Vpc(nat_gateway['VpcId'])
        subnet = ec2.Subnet(nat_gateway['SubnetId'])
        
        # Get the data usage in the last 30 days
        end_time = datetime.utcnow()
        start_time = end_time - timedelta(days=30)
        data_usage = client.get_nat_gateway_statistics(
            NatGatewayId=nat_gateway['NatGatewayId'],
            StartTime=start_time,
            EndTime=end_time
        )['NatGatewayStatistics'][0]['BytesOutFromNatGateway']
        
        # Convert data usage to GB
        data_usage_gb = round(data_usage / (1024**3), 2)
        
        # Append the NAT Gateway information to the list
        nat_gateways.append({
            'Name': nat_gateway['NatGatewayId'],
            'Region': region,
            'Subnet': subnet.cidr_block,
            'Data Usage (GB)': data_usage_gb
        })

# Create a Pandas dataframe from the NAT Gateway list
df = pd.DataFrame(nat_gateways)

# Save the dataframe to an Excel file
df.to_excel('nat_gateways.xlsx', index=False)
