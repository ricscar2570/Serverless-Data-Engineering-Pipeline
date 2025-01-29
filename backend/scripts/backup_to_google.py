from google.cloud import storage
import boto3
import os

def backup_to_google(s3_bucket, gcs_bucket):
    # Configura client AWS S3
    s3 = boto3.client("s3")
    # Configura client Google Cloud Storage
    gcs = storage.Client()

    # Lista file in S3
    objects = s3.list_objects_v2(Bucket=s3_bucket)
    for obj in objects.get("Contents", []):
        file_key = obj["Key"]
        print(f"Scaricando {file_key} da S3...")
        s3.download_file(s3_bucket, file_key, file_key)

        # Carica su GCS
        print(f"Caricando {file_key} su Google Cloud Storage...")
        bucket = gcs.bucket(gcs_bucket)
        blob = bucket.blob(file_key)
        blob.upload_from_filename(file_key)

        # Rimuovi il file locale
        os.remove(file_key)

if __name__ == "__main__":
    backup_to_google("data-lake-serverless", "gcs-data-lake")

