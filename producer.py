# producer.py
from kafka import KafkaProducer
import time
import json
import random
from faker import Faker

fake = Faker()

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

#categories = ['tech', 'finance', 'sports', 'health', 'entertainment']

for i in range(11):
    message = {
        'name': fake.name(),
        'email': fake.email(),
        'address': fake.address(),
        'phone_number': fake.phone_number(),
        'timestamp': time.time(),
 
    }
    producer.send('metadata-topic', value=message)
    print(f"Sent: {message}")
    time.sleep(1)

producer.close()
