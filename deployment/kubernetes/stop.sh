#!/bin/bash

# Folder variables
CENTRAL_FOLDER="central-bicycle-rental"
NS_FOLDER="local-bicycle-rental-ns"
SU_FOLDER="local-bicycle-rental-su"
KG_FOLDER="local-bicycle-rental-kg"
SHARED_FOLDER="shared"

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

minikube kubectl -- delete -f "$SU_FOLDER/local-bicycle-rental-su-deployment.yaml"
minikube kubectl -- delete -f "$SU_FOLDER/local-bicycle-rental-database-su-deployment.yaml"
minikube kubectl -- delete -f "$SU_FOLDER/local-bicycle-rental-su-config.yaml"
minikube kubectl -- delete -f "$SU_FOLDER/local-bicycle-rental-database-su-secret.yaml"
minikube kubectl -- delete -f "$SU_FOLDER/local-bicycle-rental-database-su-volume-claim.yaml"
minikube kubectl -- delete -f "$SU_FOLDER/local-bicycle-rental-database-su-volume.yaml"

minikube kubectl -- delete -f "$KG_FOLDER/local-bicycle-rental-kg-deployment.yaml"
minikube kubectl -- delete -f "$KG_FOLDER/local-bicycle-rental-database-kg-deployment.yaml"
minikube kubectl -- delete -f "$KG_FOLDER/local-bicycle-rental-kg-config.yaml"
minikube kubectl -- delete -f "$KG_FOLDER/local-bicycle-rental-database-kg-secret.yaml"
minikube kubectl -- delete -f "$KG_FOLDER/local-bicycle-rental-database-kg-volume-claim.yaml"
minikube kubectl -- delete -f "$KG_FOLDER/local-bicycle-rental-database-kg-volume.yaml"

# Print remaining resources
minikube kubectl -- get pods
minikube kubectl -- get pvc
minikube kubectl -- get pv
