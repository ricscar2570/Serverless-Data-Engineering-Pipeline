import boto3
import argparse

lambda_client = boto3.client("lambda")

def deploy_lambda(zip_file):
    with open(zip_file, "rb") as f:
        zip_data = f.read()
    
    response = lambda_client.update_function_code(
        FunctionName="data_ingestion_lambda",
        ZipFile=zip_data
    )
    print("Funzione Lambda aggiornata:", response)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("zip_file", help="Percorso del file ZIP da caricare")
    args = parser.parse_args()
    deploy_lambda(args.zip_file)
