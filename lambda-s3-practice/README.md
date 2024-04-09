# AWS Lambda-S3 Integration Exercise

## Steps :

#### 1. Sign in to AWS Console:
Under `Modules` section in you AWS Academy learning account you will find Sandbox environment.
Click on it and start a lab environment. Wait ~3 minutes, until your AWS environment will be ready.

#### 2. Create an S3 Bucket:

* Go to the S3 service from the AWS Management Console. 
* Click on the `Create bucket` button. 
* Enter a unique bucket name, in region us-east-1, and click `Next`. 
* Leave all other settings as default and click `Next`. 
* Review and click `Create bucket`.


#### 3. Create a Lambda Function:

* Go to the Lambda service from the AWS Management Console.
* Click on `Create function`.
* Choose `Author from scratch`.
* Give your function a name, choose the runtime Python 3.12.
* Under `Permissions`, choose `Use an existing role`. From the dropdown choose LabRole, which has necessary permissions to access S3 bucket.
* In the end click `Create function`.


#### 4. Add Trigger to Lambda Function:

* In the Function Overview field click on `Add trigger`.
* Choose `S3` from the list of triggers.
* Configure the trigger:
     1. Choose the S3 bucket you created earlier.
     2. Select the event type (e.g., `All object create events`).
* Click `Add`.

#### 5. Write Lambda Function Code:

```
import json
import boto3

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # Log the event
    print(`Received event: ` + json.dumps(event, indent=2))

    # Process the records
    for record in event['Records']:
        bucket_name = record['s3']['bucket']['name']
        object_key = record['s3']['object']['key']
        print(f`File uploaded: s3://{bucket_name}/{object_key}`)
```

* After writing the code, click `Deploy` to save your changes.


#### 6. Testing:

* Upload a file to the S3 bucket you created.
* Check the CloudWatch logs for your Lambda function to see if it was triggered and if there are any errors in execution.


_That's it! You have now created a Lambda function that will be triggered on each file upload to the specified S3 bucket. You can extend the Lambda function to perform any processing or actions you require on the uploaded files._


```In the end, export Log Events as .csv and sent me via slack. And don't forget to END LAB session.```
