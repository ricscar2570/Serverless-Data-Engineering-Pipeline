import boto3
import json
import numpy as np

endpoint_name = "your-sagemaker-endpoint"

def predict(data):
    runtime = boto3.client("sagemaker-runtime")
    payload = json.dumps({"instances": data.tolist()})
    
    response = runtime.invoke_endpoint(
        EndpointName=endpoint_name,
        ContentType="application/json",
        Body=payload
    )
    
    return json.loads(response["Body"].read().decode())

# Esempio di inferenza
data = np.random.rand(1, 5)  # Simuliamo un input di 5 feature
result = predict(data)
print(result)
