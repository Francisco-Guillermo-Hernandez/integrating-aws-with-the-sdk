from database import MongoDB
from uuid import uuid4


def lambda_handler(event, context):

    client = MongoDB(databaseName='dummy_company')

    collection = client.use_collection('myCollection')
    
    doc = { 
        'id': str(uuid4()),
        'message': 'Hello from AWS Lambda!'
    }
    
    result = collection.insert_one(doc)

    client.close()

    return {
        'statusCode': 200,
        'body': f'Document inserted with ID: {result.inserted_id}'
    }
