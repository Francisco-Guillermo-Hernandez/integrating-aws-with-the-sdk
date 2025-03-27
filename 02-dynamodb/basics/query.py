import json

from boto3 import Session
from os import environ

session = Session(profile_name='Developer')
dynamoDB_client = session.client('dynamodb')


result = dynamoDB_client.query(
    TableName=environ['WHETHER_TABLE_NAME'],
    KeyConditionExpression='ZipCode = :zipcode',
    ExpressionAttributeValues={
        ':zipcode': { 'S': '79834' },
    }
)

print(json.dumps(result, indent=3))