from boto3 import Session
from datetime import datetime as dt
from botocore import exceptions

# Let's define a custom session to use the local profile of AWS CLI
session = Session(profile_name='Developer')

# Boto3 acts as a proxy with the default session 
# but in this case is necessary to create low-level clients
s3_client = session.client('s3')

file_name = 'buckets.txt'
buckets_names = open(file_name, 'r+').read()

for bucket_name in buckets_names.split('\n'):
    
    if bucket_name != '':

        # List existing objects inside of the bucket.
        response = s3_client.list_objects(Bucket=bucket_name)
        objects = response.get('Contents')
        if objects:
        
            print(f'List all the objects inside of the bucket')
            print('-----------------------------------')

            for obj in objects:   

                print(f'Object key: {obj['Key']}')    

                try:
                    s3_client.delete_object(Bucket=bucket_name, Key=obj['Key'])
                except exceptions.ClientError as e:
                    print(f'An error occurred: {e}')

            print('-----------------------------------')
        else: 
            print('There are no files to list')    


        try:
            s3_client.delete_bucket(Bucket=bucket_name)
            file = open(file_name, 'w')
            file.write('')
            file.close()
            print(f'{bucket_name} was deleted')
        except exceptions.ClientError as e:
            print(f'An error ocurred {e}')



# Get the list_buckets response
response = s3_client.list_buckets()

print('-----------------------------------')
# Print each Buckets Name
for bucket in response['Buckets']:
    print(bucket['Name'])

print('-----------------------------------')

