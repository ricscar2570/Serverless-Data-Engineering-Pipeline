import boto3
import time

cloudwatch = boto3.client("cloudwatch")

def log_pipeline_status(pipeline_name):
    codepipeline = boto3.client("codepipeline")

    while True:
        response = codepipeline.get_pipeline_state(name=pipeline_name)
        stages = response["stageStates"]

        for stage in stages:
            stage_name = stage["stageName"]
            status = stage["latestExecution"]["status"]

            print(f"Stage: {stage_name}, Stato: {status}")

            # Invio metrica a CloudWatch
            cloudwatch.put_metric_data(
                Namespace="CodePipeline",
                MetricData=[
                    {
                        "MetricName": "PipelineStageStatus",
                        "Dimensions": [{"Name": "Stage", "Value": stage_name}],
                        "Value": 1 if status == "Succeeded" else 0,
                        "Unit": "Count",
                    }
                ],
            )

        time.sleep(60)  # Controlla ogni 60 secondi

# Avvio del monitoraggio della pipeline
log_pipeline_status("ServerlessDataPipeline")
