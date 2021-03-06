from pyspark.sql.types import StringType, IntegerType

import angelou.sparksession as S
import angelou.transformations as T

from quinn.extensions import create_df


class TestTransformations(object):

    def test_with_greeting(self):
        source_data = [
            ("jose", 1),
            ("li", 2)
        ]
        source_df = S.spark.createDataFrame(
            source_data,
            ["name", "age"]
        )

        actual_df = T.with_greeting(source_df)

        expected_data = [
            ("jose", 1, "hello!"),
            ("li", 2, "hello!")
        ]
        expected_df = S.spark.createDataFrame(
            expected_data,
            ["name", "age", "greeting"]
        )

        assert (expected_df.collect() == actual_df.collect())

    def test_with_clean_first_name(self):
        source_df = S.spark.create_df(
            [("jo&&se", "a"), ("##li", "b"), ("!!sam**", "c")],
            [("first_name", StringType(), True), ("letter", StringType(), True)]
        )
        actual_df = T.with_clean_first_name(source_df)
        expected_df = S.spark.create_df(
            [("jo&&se", "a", "jose"), ("##li", "b", "li"), ("!!sam**", "c", "sam")],
            [("first_name", StringType(), True), ("letter", StringType(), True),
             ("clean_first_name", StringType(), True)]
        )

        assert (expected_df.collect() == actual_df.collect())

    def test_with_fibonacci(self):
        source_df = S.spark.create_df(
            [("jose", 5), ("li", 10)],
            [("name", StringType(), True), ("n", IntegerType(), True)]
        )
        expected_df = S.spark.create_df(
            [("jose", 5, 5), ("li", 10, 55)],
            [("name", StringType(), True), ("n", IntegerType(), True), ("fibonacci", IntegerType(), True)]
        )
        actual_df = T.with_fibonacci(source_df)

        assert (expected_df.collect() == actual_df.collect())
