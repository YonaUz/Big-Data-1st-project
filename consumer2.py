# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 22:49:26 2021

@author: yonau
"""

import json
import time
from bson import json_util
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='192.168.33.13:9092')
topic_name='quickstart-events'

        
f = open('covid.json')
data = json.load(f)
for msg in data:
    producer.send(topic_name,json.dumps(msg).encode('utf-8'))
    for dic in data[msg]:
      # producer.send(topic_name,json.dumps(dic).encode('utf-8')) 
      producer.send(topic_name,json.dumps(data[msg][dic]).encode('utf-8')) 
      # for val in data[msg][dic]:
      #     producer.send(topic_name,json.dumps(val).encode('utf-8'))
    time.sleep(15)
    

f.close()