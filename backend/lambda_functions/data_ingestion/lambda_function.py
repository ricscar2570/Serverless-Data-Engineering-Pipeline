import json
import boto3

sagemaker_runtime = boto3.client("sagemaker-runtime")
endpoint_name = "my-endpoint"  # Sostituisci con il nome del tuo endpoint

def lambda_handler(event, context):
    # Estrai i dati di input
    data = json.loads(event["body"])
    payload = ",".join(map(str, data.values()))

    # Invoca l'endpoint SageMaker
    response = sagemaker_runtime.invoke_endpoint(
        EndpointName=endpoint_name,
        ContentType="text/csv",
        Body=payload,
    )

    # Estrai la previsione
    prediction = response["Body"].read().decode("utf-8")

    # Restituisci la previsione
    return {
        "statusCode": 200,
        "body": json.dumps({"prediction": prediction}),
    }
