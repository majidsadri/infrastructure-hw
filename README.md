# infrastructure-hw

## Your mission

For this assignment, you're going to create the infrastructure for an application with a small set of services.

- One service needs to broadcast `Hello world` at random intervals. Make the interval anywhere from 1 to 10 seconds, with each the time until the next broadcast each chosen randomly.

- Another service needs to receive the `Hello world` broadcasts.

- Then a user should be able to view the `Hello world` broadcasts, as they arrive, from a web browser.

### Other requirements

- Use whatever languages and frameworks you want to create the services.
- We're aiming to just run this application on an engineer's local machine, not the cloud; design your solution for `minikube`
- Your solution should have the minimum number of manual setup steps necessary.
- Use any adjacent infrastructure tools you think make for a more elegant solution.

## Submission

- Fork this repository on GitHub. Develop a solution on your fork. Extra points for good git hygiene.
- Include specific instructions in your README about pre-requisites and setup steps. Another engineer should be able to go from zero to running your solution on their local machine.
- Either send us the link to your repository (if you make it public) or email us a zipped-up folder.


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
kubectl apply -f kafka-cluster.yaml -n kafka
```


### Build Docker Images

You need to build the Docker images for each service before deploying them to Minikube.

```bash
# Build the broadcaster image
cd broadcaster
docker build -t hello-world-broadcaster .

# Build the receiver image
cd ../receiver
docker build -t hello-world-receiver .

# Build the web interface image
cd ../web
docker build -t hello-world-web .
```


## Deploy the Kubernetes Deployment Files

```bash

./minikube-setup.sh
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