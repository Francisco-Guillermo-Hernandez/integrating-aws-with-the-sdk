from boto3 import Session
from botocore import exceptions
from argparse import ArgumentParser

parser = ArgumentParser(description='A simple tool to delete objects from a given bucket')
parser.add_argument('profile', type=str, help='Please provide the name of your profile')
parser.add_argument('bucket_name', type=str, help='Please provide the name of the bucket')
parser.add_argument('key', type=str, help='Please provide the key of the object in the bucket')

arguments = parser.parse_args()

# Let's define a custom session to use the local profile of AWS CLI
session = Session(profile_name=arguments.profile)

# Boto3 acts as a proxy with the default session 
# but in this case is necessary to create low-level clients
s3_client = session.client('s3')

key = arguments.key

try:
    # Delete the object
    s3_client.delete_object(Bucket=arguments.bucket_name, Key=key)
    print(f'The object: {key} was deleted sucessfully.')
except exceptions.ClientError as e:
    print(f'An error occurred: {e}')