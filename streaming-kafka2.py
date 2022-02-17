from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

sc = SparkContext(appName = "PythonSparkStreamingKafka")
sc.setLogLevel("WARN")

ssc = StreamingContext(sc,10) #tps d'attente avant prochaine execution

directKafkaStream = KafkaUtils.createDirectStream(ssc, ["quickstart-events"],{"metadata.broker.list":"192.168.33.13:909$
directKafkaStream.pprint()
lines = directKafkaStream.map(lambda x : x[1])
lines.pprint(140) #pour afficher toutes les lignes 
#directKafkaStream.count().pprint()

#Starting Spark context
ssc.start()
ssc.awaitTermination()