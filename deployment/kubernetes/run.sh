#!/bin/bash

# Folder variables
CENTRAL_FOLDER="central-bicycle-rental"
NS_FOLDER="local-bicycle-rental-ns"
SU_FOLDER="local-bicycle-rental-su"
KG_FOLDER="local-bicycle-rental-kg"
SHARED_FOLDER="shared"

# Central bicycle rental
minikube kubectl -- apply -f "$CENTRAL_FOLDER/central-bicycle-rental-database-secret.yaml"
minikube kubectl -- apply -f "$CENTRAL_FOLDER/central-bicycle-rental-config.yaml"
minikube kubectl -- apply -f "$CENTRAL_FOLDER/central-bicycle-rental-database-volume.yaml"
minikube kubectl -- apply -f "$CENTRAL_FOLDER/central-bicycle-rental-database-volume-claim.yaml"
minikube kubectl -- apply -f "$CENTRAL_FOLDER/central-bicycle-rental-deployment.yaml"

# Local bicycle rentals (NS, SU, KG)
minikube kubectl -- apply -f "$NS_FOLDER/local-bicycle-rental-database-ns-secret.yaml"
minikube kubectl -- apply -f "$NS_FOLDER/local-bicycle-rental-ns-config.yaml"
minikube kubectl -- apply -f "$NS_FOLDER/local-bicycle-rental-database-ns-volume.yaml"
minikube kubectl -- apply -f "$NS_FOLDER/local-bicycle-rental-database-ns-volume-claim.yaml"
minikube kubectl -- apply -f "$NS_FOLDER/local-bicycle-rental-ns-deployment.yaml"

minikube kubectl -- apply -f "$SU_FOLDER/local-bicycle-rental-database-su-secret.yaml"
minikube kubectl -- apply -f "$SU_FOLDER/local-bicycle-rental-su-config.yaml"
minikube kubectl -- apply -f "$SU_FOLDER/local-bicycle-rental-database-su-volume.yaml"
minikube kubectl -- apply -f "$SU_FOLDER/local-bicycle-rental-database-su-volume-claim.yaml"
minikube kubectl -- apply -f "$SU_FOLDER/local-bicycle-rental-su-deployment.yaml"

minikube kubectl -- apply -f "$KG_FOLDER/local-bicycle-rental-database-kg-secret.yaml"
minikube kubectl -- apply -f "$KG_FOLDER/local-bicycle-rental-kg-config.yaml"
minikube kubectl -- apply -f "$KG_FOLDER/local-bicycle-rental-database-kg-volume.yaml"
minikube kubectl -- apply -f "$KG_FOLDER/local-bicycle-rental-database-kg-volume-claim.yaml"
minikube kubectl -- apply -f "$KG_FOLDER/local-bicycle-rental-kg-deployment.yaml"

# Shared resources
echo "Waiting for NGINX Ingress Controller to be ready..."
minikube kubectl -- wait --namespace ingress-nginx --for=condition=available deployment/ingress-nginx-controller --timeout=120s

minikube kubectl -- apply -f "$SHARED_FOLDER/ingress.yaml"
minikube kubectl -- apply -f "$SHARED_FOLDER/network-policy.yaml"

echo "All resources deployed. Pods starting..."
minikube kubectl -- get pods
