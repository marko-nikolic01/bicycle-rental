#!/bin/bash

minikube start --driver=docker --cni calico
minikube addons enable storage-provisioner
minikube addons enable ingress
eval $(minikube -p minikube docker-env)
