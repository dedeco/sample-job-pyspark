import pyspark.sql.functions as F
import quinn
from pyspark.sql.types import IntegerType

from angelou.helpers import fibo


def with_greeting(df):
    return df.withColumn("greeting", F.lit("hello!"))


def with_clean_first_name(df):
    return df.withColumn(
        "clean_first_name",
        quinn.remove_non_word_characters(F.col("first_name"))
    )


def with_fibonacci(df):
    fibonacci_udf = F.udf(lambda z: fibo(z), IntegerType())
    return df.withColumn(
        "fibonacci"
        , fibonacci_udf(F.col("n"))
    )
