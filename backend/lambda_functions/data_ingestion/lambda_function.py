from pydantic import BaseModel, ValidationError
import boto3
import json
import logging
import os

sns_client = boto3.client("sns")
s3 = boto3.client("s3")
logs_client = boto3.client("logs")

LOG_GROUP = os.getenv("LOG_GROUP_NAME", "ServerlessPipelineLogs")
LOG_STREAM = os.getenv("LOG_STREAM_NAME", "LambdaExecution")

class DataPayload(BaseModel):
    device_id: str
    value: float
    timestamp: str

def lambda_handler(event, context):
    try:
        data = json.loads(event["body"])
        validated_data = DataPayload(**data)

        s3.put_object(
            Bucket="data-lake-serverless",
            Key=f"processed-data-{validated_data.device_id}.json",
            Body=json.dumps(data)
        )

        return {"statusCode": 200, "body": "Successo"}
    
    except ValidationError as e:
        return {"statusCode": 400, "body": "Errore di validazione"}
