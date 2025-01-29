import sagemaker
from sagemaker.sklearn.estimator import SKLearn
import boto3
import os

# Configurazione
sagemaker_session = sagemaker.Session()
role = os.environ.get("SAGEMAKER_ROLE", "arn:aws:iam::your-account-id:role/service-role/AmazonSageMaker-ExecutionRole")
bucket = sagemaker_session.default_bucket()
prefix = "sagemaker-pipeline"

# Upload del dataset su S3
data_path = "s3://{}/{}/".format(bucket, prefix)
train_path = sagemaker_session.upload_data("data/test_data.csv", bucket=bucket, key_prefix=prefix)

# Creazione dell'estimator con Scikit-Learn
sklearn_estimator = SKLearn(
    entry_point="train_script.py",
    role=role,
    instance_count=1,
    instance_type="ml.m5.large",
    framework_version="0.23-1",
    sagemaker_session=sagemaker_session,
)

# Addestramento del modello
sklearn_estimator.fit({"train": train_path})
print("Modello addestrato con successo!")
