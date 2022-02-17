from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark.sql import SQLContext

sc = SparkContext(appName = "PythonSparkStreamingKafka")
sc.setLogLevel("WARN")

ssc = StreamingContext(sc,10) #tps d'attente avant prochaine execution


directKafkaStream = KafkaUtils.createDirectStream(ssc, ["quickstart-events"],{"metadata.broker.list":"192.168.33.13:9092"})

directKafkaStream.pprint()
lines = directKafkaStream.map(lambda x : x[1]) #on n'affiche pas le 'None' inutile
lines.pprint(70) #par defaut pprint affich les 10 premiers donc ajout de parametres 14 car nb lignes assez

print(lines.flatMap(lambda s:s.split()))
print(type(lines))

lines.saveAsFiles("alors")

#Starting Spark context
ssc.start()
ssc.awaitTermination()
