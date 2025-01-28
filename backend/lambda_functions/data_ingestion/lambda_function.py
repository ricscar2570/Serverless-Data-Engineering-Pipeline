import boto3
import json
import logging

sns_client = boto3.client("sns")
s3 = boto3.client("s3")
sns_topic_arn = "arn:aws:sns:<region>:<account-id>:serverless-notifications"

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    try:
        logger.info("Evento ricevuto: %s", event)

        # Parsing del payload JSON
        data = json.loads(event["body"])
        logger.info("Dati elaborati: %s", data)

        # Salva i dati su S3
        bucket_name = "data-lake-serverless"
        file_name = f"processed-data-{data['device_id']}.json"
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=json.dumps(data))

        # Notifica SNS di successo
        sns_client.publish(
            TopicArn=sns_topic_arn,
            Subject="Successo Ingestione Dati",
            Message=f"Dati elaborati per dispositivo {data['device_id']}"
        )
        return {"statusCode": 200, "body": "Successo"}

    except Exception as e:
        logger.error("Errore durante l'elaborazione: %s", str(e))
        sns_client.publish(
            TopicArn=sns_topic_arn,
            Subject="Errore Ingestione Dati",
            Message=f"Errore: {str(e)}"
        )
        return {"statusCode": 500, "body": "Errore"}
