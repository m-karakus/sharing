#!/bin/bash
# bash verison.sh prod/nginx-test-deployment.yaml "bug"

AIRFLOW_NAME="airflow-cluster"
AIRFLOW_NAMESPACE="airflow-cluster"

cd /root/prod/airflow && git reset --hard origin/main \
    && git pull origin main \
    && docker build . --tag mkarakus2/sharing:airflow-v1.0.1 \
    && docker push mkarakus2/sharing:airflow-v1.0.1

helm upgrade --install --debug \
    "$AIRFLOW_NAME" \
    airflow-stable/airflow \
    --namespace "$AIRFLOW_NAMESPACE" \
    --version "8.6.0" \
    --values ./values.yaml

cp -r /root/systems/prod/airflow/dags/. /srv/nfs/kubedata/airflow-cluster-airflow-dags-pvc-pvc-fe2ddb07-8bb5-4a45-ba94-e2eaa5af9236
