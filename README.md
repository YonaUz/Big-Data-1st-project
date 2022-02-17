# Big-Data-1st-project
Projet de récupération et d'analyse de données de covid à travers le monde.

**ETAPES A SUIVRE ** 
(après la création du topic et de l'installation de Kakfa comme expliqué ici:
https://github.com/msouidi/lectures 

# 1. Ouvrir un premier terminal (ici ca sera le producer )
cd Big-Data-1st-project\Kafka
vagrant up
vagrant ssh
cd kafka
bin/kafka-console-producer.sh --topic quickstart-events --bootstrap-server 192.168.33.13:9092 
**_________________________________________________________________________________**
# 2. Ouvrir un second terminal (ici ce sera le consumer kafka)
cd Big-Data-1st-project\Kafka
vagrant up
vagrant ssh
cd kafka
bin/kafka-console-consumer.sh --topic quickstart-events --bootstrap-server 192.168.33.13:9092
**_________________________________________________________________________________**
# 3. ouvrir un troisième terminal ( ce sera la vm Spark)
cd Big-Data-1st-project\spark
vagrant ssh
password: (le mdp lors de la création de la vm)
copier les code streaming-kafka2.py et streaming-kafka3.py avec nano et les enregistrer 
/usr/local/spark/bin/spark-submit streaming-kafka1.py pour lancer le script
-> pour lancer le code python cree 
les donnéees vont apparaitre 
