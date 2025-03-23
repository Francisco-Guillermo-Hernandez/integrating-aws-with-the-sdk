from boto3 import Session, client
from os import environ as env


aws_environment = env['AWS_ENVIRONMENT']

def lambda_handler(event, context):

    # Create an S3 client
    if aws_environment == 'local':
        session = Session(profile_name='Developer')
        s3_client = session.client('s3')
    else:
        s3_client = client('s3')
    

    # List all S3 buckets
    response = s3_client.list_buckets()

    # Extract bucket names from the response
    bucket_names = [bucket['Name'] for bucket in response['Buckets']]

    # Print the bucket names
    print('S3 Buckets:')
    for name in bucket_names:
        print(f"- {name}")

    # Return the list of bucket names
    return {
        'headers': {
            'content-type': 'application/json',
        },
        'statusCode': 200,
        'body': {
            'bucket_names': bucket_names
        }
    }



if __name__ == "__main__" and aws_environment == 'local':
    result = lambda_handler(None, None)
    print(result)