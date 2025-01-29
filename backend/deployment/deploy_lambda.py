import boto3

lambda_client = boto3.client("lambda")

def deploy_lambda():
    with open("lambda_function.zip", "rb") as f:
        zip_data = f.read()

    response = lambda_client.update_function_code(
        FunctionName="data_ingestion_lambda",
        ZipFile=zip_data
    )
    print("Funzione Lambda aggiornata:", response)

if __name__ == "__main__":
    deploy_lambda()

