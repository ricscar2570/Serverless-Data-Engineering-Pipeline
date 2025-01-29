import sagemaker
import boto3
import os
from sagemaker.automl.automl import AutoML

sagemaker_session = sagemaker.Session()
role = os.environ.get("SAGEMAKER_ROLE", "arn:aws:iam::your-account-id:role/service-role/AmazonSageMaker-ExecutionRole")
bucket = sagemaker_session.default_bucket()
prefix = "sagemaker-autopilot"

# Upload dataset
train_path = sagemaker_session.upload_data("data/test_data.csv", bucket=bucket, key_prefix=prefix)

# Configurazione SageMaker Autopilot
auto_ml = AutoML(
    role=role,
    target_attribute_name="label",  # Nome della colonna target
    max_candidates=10,  # Numero massimo di modelli da testare
    problem_type="BinaryClassification",
    job_objective={"MetricName": "F1"},
    sagemaker_session=sagemaker_session,
)

# Avvio del training con Autopilot
auto_ml.fit(inputs=train_path, wait=True)
print("AutoML completato. Modelli migliori selezionati!")
