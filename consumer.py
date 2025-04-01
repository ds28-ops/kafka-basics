# consumer.py
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'metadata-topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='metadata-group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("Waiting for messages...")
for message in consumer:
    data = message.value
    #print(f"[{data['timestamp']}] [{data['category'].upper()}] {data['headline']} - {data['author']}")
    print(f"{data['name']}\n{data['email']}\n{data['address']}\n{data['phone_number']}")
    print("--------------------------------------------------")
    #print("--------------------------------------------------")
