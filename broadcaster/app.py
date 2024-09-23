import time
import random
from kafka import KafkaProducer

# producer = KafkaProducer(bootstrap_servers='kafka:9092')

# producer = KafkaProducer(bootstrap_servers='my-cluster-kafka-bootstrap:9092')

producer = KafkaProducer(bootstrap_servers='my-cluster-kafka-bootstrap.kafka.svc.cluster.local:9092')



def broadcast():
    while True:
        message = b'Hello world'
        producer.send('hello-world-topic', message)
        print(f"Sent: {message}")
        sleep_time = random.randint(1, 10)
        time.sleep(sleep_time)

if __name__ == "__main__":
    broadcast()
