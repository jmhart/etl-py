from pyspark.sql import SparkSession


def extract(source):
    print("Extract...")

    print("Creating spark session...")
    spark = SparkSession.builder.appName("reading csv").getOrCreate()

    print("Read source...")
    output = spark.read.format("CSV").options(
        header=True, inferSchema=True).load(source)
    print(output)

    return output
