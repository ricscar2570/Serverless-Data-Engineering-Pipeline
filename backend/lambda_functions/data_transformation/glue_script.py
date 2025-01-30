from pyspark.sql.functions import lit
import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext

glueContext = GlueContext(SparkContext.getOrCreate())
spark = glueContext.spark_session

data_frame = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": ["s3://data-lake-serverless/raw-data/"]},
    format="json"
)

transformed_data = data_frame.toDF().withColumn("processed", lit(True))
transformed_data.write.mode("overwrite").json("s3://data-lake-serverless/processed-data/")
