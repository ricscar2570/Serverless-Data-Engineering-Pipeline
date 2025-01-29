import boto3
import json
import logging

# Configurazione Logging CloudWatch
logger = logging.getLogger()
logger.setLevel(logging.INFO)

cloudwatch_logs = boto3.client("logs")
log_group_name = "/aws/sagemaker/inference"
log_stream_name = "InferenceLogs"

endpoint_name = "your-sagemaker-endpoint"

def predict(data):
    runtime = boto3.client("sagemaker-runtime")
    payload = json.dumps({"instances": data.tolist()})

    # Chiamata a SageMaker
    response = runtime.invoke_endpoint(
        EndpointName=endpoint_name,
        ContentType="application/json",
        Body=payload
    )

    result = json.loads(response["Body"].read().decode())

    # Invio dei log a CloudWatch
    log_event = {
        "logGroupName": log_group_name,
        "logStreamName": log_stream_name,
        "logEvents": [
            {
                "timestamp": int(boto3.client("sts").get_caller_identity()["Account"]),
                "message": json.dumps({"input": data.tolist(), "output": result}),
            }
        ],
    }

    cloudwatch_logs.put_log_events(**log_event)
    logger.info(f"Inferenza completata: {result}")

    return result

# Esempio di inferenza
import numpy as np
data = np.random.rand(1, 5)  # Simuliamo un input di 5 feature
result = predict(data)
print(result)
