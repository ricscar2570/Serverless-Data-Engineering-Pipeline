import boto3
import requests
import time

s3_client = boto3.client("s3")
lambda_client = boto3.client("lambda")
bucket_name = "data-lake-serverless-demo"

def test_ingestion_api():
    api_url = "https://your-api-endpoint/data-ingestion"
    test_data = {
        "device_id": "101",
        "value": 42.5,
        "timestamp": "2025-01-01T12:00:00"
    }

    response = requests.post(api_url, json=test_data)
    assert response.status_code == 200

def test_data_in_s3():
    # Attendi il completamento del job
    time.sleep(10)

    response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix="processed/")
    assert "Contents" in response
    assert len(response["Contents"]) > 0

def test_dashboard_data():
    dashboard_api = "https://your-dashboard-api/data"
    response = requests.get(dashboard_api)
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
