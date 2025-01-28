import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    for record in event["Records"]:
        payload = json.loads(record["kinesis"]["data"])
        logger.info(f"Dati ricevuti: {payload}")

        # Logica di elaborazione del record
        # Qui puoi implementare ulteriori operazioni sul payload

