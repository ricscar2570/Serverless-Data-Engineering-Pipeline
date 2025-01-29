import boto3
import json
import logging

# Configurazione Logging CloudWatch
logger = logging.getLogger()
logger.setLevel(logging.INFO)

endpoint_name = "your-sagemaker-endpoint"

def lambda_handler(event, context):
    runtime = boto3.client("sagemaker-runtime")
    body = json.loads(event["body"])
    payload = json.dumps({"instances": body["data"]})

    # Chiamata all'endpoint SageMaker
    response = runtime.invoke_endpoint(
        EndpointName=endpoint_name,
        ContentType="application/json",
        Body=payload
    )

    result = json.loads(response["Body"].read().decode())

    # Invio Log a CloudWatch
    logger.info(f"Richiesta ricevuta: {body['data']}")
    logger.info(f"Risultato inferenza: {result}")

    return {
        "statusCode": 200,
        "body": json.dumps(result)
    }
