from kafka import KafkaConsumer
import json
import socket

consumer= KafkaConsumer(
    'multi-partition-topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='partition-demo-group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

consumer_id= socket.gethostname()

print(f"Consumer ID: {consumer_id} started")

for message in consumer:
    partition=message.partition
    data=message.value
    print(f"Partition: {partition}")
    print(f"{data['id']}\n {data['category']}\n {data['headline']}")
    print("--------------------------------------------------")