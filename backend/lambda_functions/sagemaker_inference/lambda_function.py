import boto3
import json

endpoint_name = "your-sagemaker-endpoint"

def lambda_handler(event, context):
    runtime = boto3.client("sagemaker-runtime")
    
    body = json.loads(event["body"])
    payload = json.dumps({"instances": body["data"]})
    
    response = runtime.invoke_endpoint(
        EndpointName=endpoint_name,
        ContentType="application/json",
        Body=payload
    )
    
    return {
        "statusCode": 200,
        "body": json.loads(response["Body"].read().decode())
    }
