# producer_partitioned.py
from kafka import KafkaProducer
import time
import json
import random
from faker import Faker

fake=Faker()
producer=KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

for i in range(16):
    category = random.choice(['sports', 'tech', 'politics'])
    message = {
        'id':i,
        'category': category,
        'headline': fake.sentence(),
    }
    key=category.encode('utf-8')
    producer.send('multi-partition-topic', key=key, value=message)
    print(f"Sent: {message}")
    time.sleep(1)
producer.close()
