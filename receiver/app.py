from kafka import KafkaConsumer

# consumer = KafkaConsumer('hello-world-topic', bootstrap_servers='my-cluster-kafka-bootstrap.kafka.svc.cluster.local:9092')

consumer = KafkaConsumer(
    'hello-world-topic',
    bootstrap_servers='my-cluster-kafka-bootstrap.kafka.svc.cluster.local:9092',
    api_version=(3, 7, 0)  # Set the API version to match your Kafka broker version
)


def receive():
    for message in consumer:
        print(f"Received: {message.value.decode('utf-8')}")

if __name__ == "__main__":
    receive()
