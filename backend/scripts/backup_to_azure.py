import boto3
import subprocess

s3 = boto3.client("s3")
bucket_name = "data-lake-serverless"

def sync_to_azure():
    # Scarica i file da S3
    response = s3.list_objects_v2(Bucket=bucket_name)
    for obj in response.get("Contents", []):
        file_key = obj["Key"]
        s3.download_file(bucket_name, file_key, f"/tmp/{file_key}")
        
        # Carica su Azure Blob Storage
        subprocess.run([
            "az", "storage", "blob", "upload",
            "--container-name", "multi-cloud-backup",
            "--account-name", "<account_name>",
            "--name", file_key,
            "--file", f"/tmp/{file_key}"
        ])
        print(f"File {file_key} sincronizzato su Azure Blob Storage.")

if __name__ == "__main__":
    sync_to_azure()

