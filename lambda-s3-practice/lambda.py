import json
import boto3

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # Log the event
    print("Received event: " + json.dumps(event, indent=2))

    # Process the records
    for record in event['Records']:
        bucket_name = record['s3']['bucket']['name']
        object_key = record['s3']['object']['key']
        print(f"File uploaded: s3://{bucket_name}/{object_key}")

