import json
import boto3

def starthere(event, context):
    # Code to run here
    msg="Hello world"

    return {
            'statusCode': 200,
            'body': json.dumps(msg)
    }
