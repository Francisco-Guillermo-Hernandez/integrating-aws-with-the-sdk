from boto3 import Session
from datetime import datetime as dt
from botocore import exceptions

# Let's define a custom session to use the local profile of AWS CLI
session = Session(profile_name='Developer')

# Boto3 acts as a proxy with the default session 
# but in this case is necessary to create low-level clients
s3_client = session.client('s3')

# Let's define a unique name for the bucket
bucket_name = f'photos-of-plushies-{ dt.now().strftime("%Y-%m-%d-%H-%M-%S") }'

try: 
    # Creates a new bucket with a unique name
    s3_client.create_bucket(Bucket=bucket_name)
except exceptions.ClientError as e:
    print(f'An error occurred {e}')

# List the buckets to show the new
buckets = s3_client.list_buckets()

print('-----------------------------------')

for bucket in buckets['Buckets']:
    print(bucket['Name'])
    
print('-----------------------------------')

file_name = 'Hisuian-Zorua.jpg' 
key = 'photos/Hisuian-Zorua.jpg'

extra_args = {
    'ContentType': 'image/jpeg',
    'Metadata': {
        'Name': 'Hisuian Zorua',
        'Stage': 'UnEvolved',
        'types': 'Normal,Ghost',
        'Ability': 'Illusion',
    }
}

try:
    # This method is handled by the S3 Transfer Manager, 
    # it means it is going to handle multipart upload underneath.
    s3_client.upload_file(
        Bucket=bucket_name, 
        Filename=file_name, 
        Key=key,
        ExtraArgs=extra_args
    )
except exceptions.ClientError as e:
    print(f'An error occurred {e}')


# List existing objects inside of the bucket.
response = s3_client.list_objects(Bucket=bucket_name)

for obj in response['Contents']:
    print(obj['Key'])


# Let's retrieve the metadata from the object without returning the object itself.
response = s3_client.head_object(Bucket=bucket_name, Key=key)
print('-----------------------------------')
print(f'ContentLength: {response['ContentLength']}')
print(f'ContentType: {response['ContentType']}')

print('-----------------------------------')
for key, val in response['Metadata'].items():
    print(f'{key}: {val}')

print('-----------------------------------')

file = open('buckets.txt', '+a')
file.write(f'{bucket_name}\n')
file.close()