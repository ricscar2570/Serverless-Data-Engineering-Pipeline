import sagemaker
from sagemaker.sklearn.model import SKLearnModel
import boto3
import os

sagemaker_session = sagemaker.Session()
role = os.environ.get("SAGEMAKER_ROLE", "arn:aws:iam::your-account-id:role/service-role/AmazonSageMaker-ExecutionRole")

# Percorso del modello su S3
bucket = sagemaker_session.default_bucket()
prefix = "sagemaker-pipeline/model"
model_path = "s3://{}/{}".format(bucket, prefix)

# Deploy del modello come endpoint SageMaker
sklearn_model = SKLearnModel(
    model_data=model_path,
    role=role,
    entry_point="train_script.py",
    framework_version="0.23-1",
    sagemaker_session=sagemaker_session,
)

predictor = sklearn_model.deploy(instance_type="ml.m5.large", initial_instance_count=1)
print(f"Modello deployato su {predictor.endpoint_name}")
