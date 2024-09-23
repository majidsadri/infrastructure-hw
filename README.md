# infrastructure-hw


# Hello World Broadcast Application

This project demonstrates a simple Kafka-based message broadcasting application that consists of three services:
- **Broadcaster**: Sends "Hello World" messages at random intervals.
- **Receiver**: Listens for and processes the "Hello World" messages.
- **Web Interface**: Displays the received messages in real-time using a web browser.

The application runs locally using Minikube, Docker, and Kafka for message passing.

## Prerequisites

Make sure you have the following tools installed:
- Docker
- Minikube
- Kubernetes CLI (`kubectl`)

## Instructions


### Kafka Cluster

```bash
kubectl apply -f kafka.yaml -n kafka
```


### Build Docker Images

You need to build the Docker images for each service before deploying them to Minikube.

```bash
# Build the broadcaster image
cd broadcaster
docker build -t broadcaster:latest .

# Build the receiver image
cd ../receiver
docker build -t receiver:latest .

# Build the web interface image
cd ../web
docker build -t web:latest .
```


## Deploy the Kubernetes Deployment Files

```bash

./minikube-setup.sh
```

## Run Web console

```bash

kubectl port-forward svc/web-service 5000:500
```


## Project Structure

```bash
hello-world-kafka-project/
│
├── broadcaster/                      # Kafka broadcaster service
│   ├── Dockerfile                     # Dockerfile to build broadcaster image
│   └── app.py                    # Code for broadcasting messages
│
├── receiver/                         # Kafka receiver service
│   ├── Dockerfile                     # Dockerfile to build receiver image
│   └── app.py                    # Code for receiving messages
│
├── web/                              # Web service for displaying messages
│   ├── Dockerfile                     # Dockerfile to build web service image
│   ├── app.py                         # Flask app with WebSocket support
│   └── templates/                     # HTML templates
│       └── index.html                 # Web interface for viewing messages
│
├── k8s/                              # Kubernetes deployment manifests
│   ├── kafka-deployment.yaml             # Kafka cluster configuration (Strimzi)
│   ├── broadcaster-deployment.yaml       # Deployment for the broadcaster service
│   ├── receiver-deployment.yaml       # Deployment for the receiver service
│   ├── web-deployment.yaml            # Deployment for the web service
│
├── minikube-setup.sh                 # Script to setup Minikube and deploy services
├── README.md                         # Project documentation
```