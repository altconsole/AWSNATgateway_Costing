# AWSNATgateway_Costing
The following code runs with Python and connects to AWS account. The code runs and calculates the AWS bill for NAT gateways across all AWS regions. 

This script retrieves data usage information for NAT Gateways in all available AWS regions and saves the data to an Excel file for analysis and reporting. It uses the Boto3 library to interact with AWS services and Pandas for data handling and manipulation.

Prerequisites

Before running the script, ensure you have the following:
AWS CLI and Boto3 installed: Make sure you have the AWS CLI and Boto3 library installed and configured with valid credentials.
Python and required libraries: The script requires Python and the following libraries to be installed:

boto3: For interacting with AWS services.
pandas: For handling and manipulating data.
openpyxl: For writing data to Excel files.
You can install these libraries using pip:

pip install boto3 pandas openpyxl

Configuration
AWS Profile: Set the desired AWS profile name in the script where indicated. This profile should have appropriate permissions to access EC2 resources and describe NAT Gateways.
Region: Modify the region_name variable to set the AWS region where you want to collect NAT Gateway data.

How the Script Works

The script performs the following steps:
Initialize AWS session and EC2 client using the provided profile name and region.
Get a list of all available AWS regions.
Loop through each region and create an EC2 resource for that region.
Retrieve all NAT Gateways in the current region.
For each NAT Gateway, get the VPC and Subnet information.
Calculate the data usage of each NAT Gateway in the last 30 days.
Convert data usage to gigabytes (GB).
Store NAT Gateway information, including name, region, subnet, and data usage in GB, in a list.
Create a Pandas DataFrame from the list.
Save the DataFrame to an Excel file named "nat_gateways.xlsx" in the current working directory.

The script will connect to AWS, fetch data usage for NAT Gateways in all regions, and save the information to the "nat_gateways.xlsx" Excel file.

Note
Ensure that the AWS profile you provided has the necessary permissions to describe NAT Gateways and their associated resources.
If you encounter any issues or errors during script execution, check the AWS credentials, permissions, and data availability for NAT Gateways in each region.
The script will overwrite any existing "nat_gateways.xlsx" file in the current working directory. Make sure to back up the previous file if needed.
For larger deployments, consider pagination and rate-limiting mechanisms to avoid throttling issues while retrieving data from AWS APIs.
