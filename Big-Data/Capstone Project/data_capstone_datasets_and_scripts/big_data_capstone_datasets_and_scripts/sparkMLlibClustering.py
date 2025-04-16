from pyspark.sql import SparkSession
from pyspark.ml.clustering import KMeans
from pyspark.ml.feature import VectorAssembler

# Initialize Spark (modern version)
spark = SparkSession.builder \
    .appName("PlayerSegmentation") \
    .config("spark.executor.memory", "4g") \
    .getOrCreate()

# Load data from new source (Cookie Cats dataset)
df = spark.read.csv("s3://your-bucket/cookie_cats_ab_test.csv", 
                   header=True, 
                   inferSchema=True)

# Feature engineering (matching original structure)
df = df.withColumn("adCount", F.when(F.col("ad_click") == True, 1).otherwise(0))
df = df.withColumn("gameClickSum", F.col("game_clicks"))
df = df.withColumn("revenue", F.col("spend_amount"))

# Aggregation (same logic as original)
agg_df = df.groupBy("user_id") \
    .agg(F.sum("adCount").alias("totalAdClicks"),
         F.sum("revenue").alias("revenue"),
         F.count("gameClickSum").alias("gameClickSum"))

# Prepare features vector
assembler = VectorAssembler(
    inputCols=["totalAdClicks", "revenue", "gameClickSum"],
    outputCol="features")

# K-means clustering (modern API)
kmeans = KMeans(k=3, seed=42, featuresCol="features")
model = kmeans.fit(assembler.transform(agg_df))

# Get centers (matches original output format)
centers = model.clusterCenters()
for center in centers:
    print(f"Cluster Center: {center}")

# Output matches original table structure
result = model.transform(assembler.transform(agg_df))
result.select("user_id", "prediction").show(5)