#!/bin/bash

# Folder variables
CENTRAL_FOLDER="central-bicycle-rental"
NS_FOLDER="local-bicycle-rental-ns"

# Shared resources
minikube kubectl -- delete -f "$SHARED_FOLDER/ingress.yaml"
minikube kubectl -- delete -f "$SHARED_FOLDER/network-policy.yaml"

# Central bicycle rental
minikube kubectl -- delete -f "$CENTRAL_FOLDER/central-bicycle-rental-deployment.yaml"
minikube kubectl -- delete -f "$CENTRAL_FOLDER/central-bicycle-rental-database-deployment.yaml"
minikube kubectl -- delete -f "$CENTRAL_FOLDER/central-bicycle-rental-config.yaml"
minikube kubectl -- delete -f "$CENTRAL_FOLDER/central-bicycle-rental-database-secret.yaml"
minikube kubectl -- delete -f "$CENTRAL_FOLDER/central-bicycle-rental-database-volume-claim.yaml"
minikube kubectl -- delete -f "$CENTRAL_FOLDER/central-bicycle-rental-database-volume.yaml"

# Local bicycle rentals (NS, SU, KG)
minikube kubectl -- delete -f "$NS_FOLDER/local-bicycle-rental-ns-deployment.yaml"
minikube kubectl -- delete -f "$NS_FOLDER/local-bicycle-rental-database-ns-deployment.yaml"
minikube kubectl -- delete -f "$NS_FOLDER/local-bicycle-rental-ns-config.yaml"
minikube kubectl -- delete -f "$NS_FOLDER/local-bicycle-rental-database-ns-secret.yaml"
minikube kubectl -- delete -f "$NS_FOLDER/local-bicycle-rental-database-ns-volume-claim.yaml"
minikube kubectl -- delete -f "$NS_FOLDER/local-bicycle-rental-database-ns-volume.yaml"

# Print remaining resources
minikube kubectl -- get pods
minikube kubectl -- get pvc
minikube kubectl -- get pv
