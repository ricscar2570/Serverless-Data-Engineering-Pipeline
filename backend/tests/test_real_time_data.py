import boto3

kinesis = boto3.client("kinesis")
stream_name = "staging-data-stream"

def test_kinesis_stream_exists():
    response = kinesis.describe_stream(StreamName=stream_name)
    assert response["StreamDescription"]["StreamStatus"] == "ACTIVE"

def test_send_data_to_stream():
    response = kinesis.put_record(
        StreamName=stream_name,
        Data='{"device_id": "101", "value": 42.5, "timestamp": "2025-01-27T12:00:00"}',
        PartitionKey="101"
    )
    assert response["ResponseMetadata"]["HTTPStatusCode"] == 200
