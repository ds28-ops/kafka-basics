

---


# Apache Kafka Basics: Self-Learning Project

This project is a self-learning exercise to understand and implement the core concepts of **Apache Kafka** using Docker, Python producers/consumers, and message partitioning.

---

## 🧠 What I Learned

- Running Kafka and Zookeeper using Docker Compose
- Writing Python-based Kafka **producers** and **consumers**
- Understanding **topic partitioning**, **consumer groups**, and **key-based message routing**
- Using the **Faker** library to generate mock data for messages
- Observing how Kafka distributes messages across partitions and consumers

---

## 🧱 Project Structure

```
.
├── compose.yml
├── producer.py
├── consumer.py
├── producer_partitioned.py
├── consumer_1.py
├── consumer_2.py
└── consumer_3.py
```

---

## 🚀 How to Run

### 1. Start Kafka and Zookeeper

```bash
docker compose up -d
```

> Uses Confluent Kafka 7.2.1

---

### 2. Basic Producer & Consumer Example

#### Run the producer
```bash
python producer.py
```

Sends random user metadata to topic: `metadata-topic`

#### Run the consumer
```bash
python consumer.py
```

Reads from the same topic and prints user data.

---

### 3. Partitioned Producer & Consumers

#### Run the partitioned producer
```bash
python producer_partitioned.py
```

Sends categorized messages (e.g., `sports`, `tech`, `politics`) to topic: `multi-partition-topic` using category as the **key**.

#### Run the consumers (in separate terminals)

```bash
python consumer_1.py
python consumer_2.py
python consumer_3.py
```

Each consumer joins the same **consumer group** (`partition-demo-group`), and Kafka load-balances partitions across them.

---

## 🔍 Key Concepts Demonstrated

- **Topics**: `metadata-topic`, `multi-partition-topic`
- **Partitioning**: Key-based message routing to partitions
- **Consumer Groups**: Demonstrated with multiple consumers balancing the workload
- **Serialization**: JSON messages with `Faker` data
- **Docker Setup**: Minimal `compose.yml` for Kafka and Zookeeper

---

## 📦 Dependencies

Install the required libraries:

```bash
pip install kafka-python faker
```

---

## 🧹 Cleanup

To stop and remove Kafka/Zookeeper containers:

```bash
docker compose down --remove-orphans
```

To forcibly remove Kafka containers:

```bash
docker rm -f kafka-basics-kafka-1 kafka-basics-zookeeper-1
```






```

