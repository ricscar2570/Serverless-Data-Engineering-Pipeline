import sagemaker
from sagemaker.sklearn.estimator import SKLearn
import boto3
import os

sagemaker_session = sagemaker.Session()
role = os.environ.get("SAGEMAKER_ROLE", "arn:aws:iam::your-account-id:role/service-role/AmazonSageMaker-ExecutionRole")
bucket = sagemaker_session.default_bucket()
prefix = "sagemaker-pipeline"

# Upload dataset su S3
train_path = sagemaker_session.upload_data("data/test_data.csv", bucket=bucket, key_prefix=prefix)

# Configurazione Spot Instances
spot_config = {"MaxWaitTimeInSeconds": 3600, "MaxRuntimeInSeconds": 1800}

sklearn_estimator = SKLearn(
    entry_point="train_script.py",
    role=role,
    instance_count=1,
    instance_type="ml.m5.large",
    framework_version="0.23-1",
    sagemaker_session=sagemaker_session,
    use_spot_instances=True,  # ✅ Spot Instances Attivate
    max_wait=spot_config["MaxWaitTimeInSeconds"],  # Tempo massimo di attesa per l'istanza Spot
    max_run=spot_config["MaxRuntimeInSeconds"],  # Tempo massimo di esecuzione del training
)

# Avvio del training
sklearn_estimator.fit({"train": train_path})
print("Modello addestrato con Spot Instances con successo!")
