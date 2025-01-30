import os
import boto3
from google.cloud import storage

s3 = boto3.client("s3")
bucket_name = os.getenv("AWS_S3_BUCKET", "data-lake-serverless")
gcs_bucket = os.getenv("GCS_BUCKET", "gcs-data-lake")

def backup_to_google():
    gcs = storage.Client()
    objects = s3.list_objects_v2(Bucket=bucket_name)
    
    for obj in objects.get("Contents", []):
        file_key = obj["Key"]
        s3.download_file(bucket_name, file_key, file_key)
        
        bucket = gcs.bucket(gcs_bucket)
        blob = bucket.blob(file_key)
        blob.upload_from_filename(file_key)
        os.remove(file_key)

if __name__ == "__main__":
    backup_to_google()
