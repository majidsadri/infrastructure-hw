#!/bin/bash

# Start minikube
minikube start

# Install Strimzi Kafka operator
kubectl create ns kafka
kubectl apply -f 'https://strimzi.io/install/latest?namespace=kafka' -n kafka

# Apply Kafka and services
kubectl apply -f kubernetes/kafka-deployment.yaml -n kafka
kubectl apply -f kubernetes/kafka-topic.yaml -n kafka

# Deploy broadcaster, receiver, and web
kubectl apply -f kubernetes/broadcaster-deployment.yaml
kubectl apply -f kubernetes/receiver-deployment.yaml
kubectl apply -f kubernetes/web-deployment.yaml

# Expose the web service
minikube service web-service
