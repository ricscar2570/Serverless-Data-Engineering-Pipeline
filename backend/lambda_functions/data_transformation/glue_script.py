import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

glueContext = GlueContext(SparkContext.getOrCreate())
spark = glueContext.spark_session

# Lettura dei dati grezzi da S3
data_frame = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": ["s3://data-lake-serverless/raw-data/"]},
    format="json"
)

# Trasformazione dei dati
transformed_data = data_frame.toDF().withColumn("processed", lit(True))

# Salvataggio dei dati trasformati
transformed_data.write.mode("overwrite").json("s3://data-lake-serverless/processed-data/")

