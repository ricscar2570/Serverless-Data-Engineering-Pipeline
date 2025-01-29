import boto3

client = boto3.client("codepipeline")

response = client.create_pipeline(
    pipeline={
        "name": "ServerlessDataPipeline",
        "roleArn": "arn:aws:iam::your-account-id:role/AWS-CodePipeline-Service-Role",
        "artifactStore": {
            "type": "S3",
            "location": "your-s3-bucket-name",
        },
        "stages": [
            {
                "name": "Source",
                "actions": [
                    {
                        "name": "SourceAction",
                        "actionTypeId": {
                            "category": "Source",
                            "owner": "AWS",
                            "provider": "CodeCommit",
                            "version": "1",
                        },
                        "outputArtifacts": [{"name": "SourceOutput"}],
                        "configuration": {"RepositoryName": "ServerlessDataPipeline", "BranchName": "main"},
                    }
                ],
            },
            {
                "name": "Build",
                "actions": [
                    {
                        "name": "BuildAction",
                        "actionTypeId": {
                            "category": "Build",
                            "owner": "AWS",
                            "provider": "CodeBuild",
                            "version": "1",
                        },
                        "inputArtifacts": [{"name": "SourceOutput"}],
                        "outputArtifacts": [{"name": "BuildOutput"}],
                        "configuration": {"ProjectName": "ServerlessDataPipeline-Build"},
                    }
                ],
            },
            {
                "name": "Deploy",
                "actions": [
                    {
                        "name": "DeployAction",
                        "actionTypeId": {
                            "category": "Deploy",
                            "owner": "AWS",
                            "provider": "CodeDeploy",
                            "version": "1",
                        },
                        "inputArtifacts": [{"name": "BuildOutput"}],
                        "configuration": {"ApplicationName": "ServerlessDataPipeline-App"},
                    }
                ],
            },
        ],
    }
)

print("Pipeline CodePipeline creata con successo!")
