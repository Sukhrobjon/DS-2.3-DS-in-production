# import findspark
# findspark.init('/path/to/spark_home')
from pyspark.mllib.regression import LinearRegressionWithSGD as lrSGD
from pyspark.mllib.regression import LabeledPoint
from pyspark.sql import SparkSession
from pyspark import SparkContext
sc = SparkContext()

spark = SparkSession \
    .builder \
    .appName("Python Spark regression example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
