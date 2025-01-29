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

# Logging avanzato su CloudWatch
log_group_name = "/aws/sagemaker/training"
log_stream_name = "SageMakerTrainingLogs"

# Configurazione Logging per SageMaker
sklearn_estimator = SKLearn(
    entry_point="train_script.py",
    role=role,
    instance_count=1,
    instance_type="ml.m5.large",
    framework_version="0.23-1",
    sagemaker_session=sagemaker_session,
    use_spot_instances=True,
    max_wait=3600,
    max_run=1800,
    enable_sagemaker_metrics=True,  # ✅ Attiva metriche avanzate
    hyperparameters={"sagemaker_program": "train_script.py"},
    output_path="s3://{}/{}".format(bucket, prefix),
    debug_hook_config={"S3OutputPath": "s3://{}/debugger/".format(bucket)},
)

# Avvio del training
sklearn_estimator.fit({"train": train_path})
print(f"Training SageMaker completato! Log disponibili su {log_group_name}")
