import logging

from faker import Factory
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

import angelou.transformations as T

faker = Factory.create()


def fake_name():
    return faker.name()


def fake_int():
    return faker.pyint(0, 50)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    spark = (SparkSession.builder
             .appName("sample-job")
             .getOrCreate())

    schema = StructType([
        StructField("name", StringType(), True),
        StructField("n", IntegerType(), True),
    ])

    data = [(fake_name(), fake_int()) for _ in range(5)]

    sample_df = spark.createDataFrame(
        data,
        schema=schema
    )

    logging.info(sample_df.show())

    result_df = T.with_fibonacci(sample_df)
    result_df.collect()

    logging.info(result_df.show(truncate=False))

    logging.info("jon finished!")
