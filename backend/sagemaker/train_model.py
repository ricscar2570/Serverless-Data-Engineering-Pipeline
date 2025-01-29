import boto3
import sagemaker
from sagemaker.inputs import TrainingInput
from sagemaker.estimator import Estimator

# Configura SageMaker
sagemaker_session = sagemaker.Session()
bucket = "data-lake-serverless"  # Sostituisci con il nome del tuo bucket S3
prefix = "processed-data"  # Sostituisci con il prefisso del percorso dei dati in S3
role = "arn:aws:iam::<account-id>:role/sagemaker-role"  # Sostituisci con il ruolo IAM per SageMaker

# Definisci l'algoritmo di training
container = "ecr.aws/sagemaker-python-sklearn:latest"  # Esempio con scikit-learn
instance_type = "ml.m5.large"  # Tipo di istanza EC2 per il training

# Definisci i dati di training
train_input = TrainingInput(
    f"s3://{bucket}/{prefix}/train", content_type="text/csv"
)

# Crea un estimator SageMaker
estimator = Estimator(
    container,
    role,
    instance_count=1,
    instance_type=instance_type,
    output_path=f"s3://{bucket}/{prefix}/output",
    sagemaker_session=sagemaker_session,
)

# Avvia il training
estimator.fit({"train": train_input})

# Salva il modello
model_name = "my-model"
model = estimator.create_model()
model.save(model_name)
