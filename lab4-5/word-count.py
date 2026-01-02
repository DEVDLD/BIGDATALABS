import pyspark
from pyspark.sql import SparkSession

# Création de la session Spark
spark = SparkSession.builder.master("yarn").appName('wordcount').getOrCreate()

# Lecture du fichier texte depuis HDFS
data = spark.sparkContext.textFile("hdfs://hadoop-master:9000/user/root/web_input/alice.txt")

# Découpage des lignes en mots
words = data.flatMap(lambda line: line.split(" "))

# Comptage des occurrences des mots
wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)

# Sauvegarde des résultats dans un répertoire HDFS
wordCounts.saveAsTextFile("hdfs://hadoop-master:9000/user/root/output/rr2")
