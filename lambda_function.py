import json

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello, this is a blue-green deployment Lambda function!",
            "input": event,
        }),
    }
