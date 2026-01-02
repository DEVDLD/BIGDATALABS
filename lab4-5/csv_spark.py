df = spark.read.csv("/content/transactions.csv", header=True, inferSchema=True)
df.show(5)