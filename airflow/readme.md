link: https://github.com/airflow-helm/charts/blob/main/charts/airflow/docs/guides/quickstart.md


## add this helm repository
helm repo add airflow-stable https://airflow-helm.github.io/charts

## update your helm repo cache
helm repo update

## set the release-name & namespace
export AIRFLOW_NAME="airflow-cluster"
export AIRFLOW_NAMESPACE="airflow-cluster"

## go to folder
cd /root/prod/airflow

## volume
kubectl apply -f volumeclaim.yaml --namespace "$AIRFLOW_NAMESPACE"

## git reset
cd /root/prod/airflow && git reset --hard origin/main \
    && git pull origin main \
    && docker build . --tag mkarakus2/sharing:airflow-v1.0.1 \
    && docker push mkarakus2/sharing:airflow-v1.0.1


## install airflow
helm upgrade --install --debug \
  "$AIRFLOW_NAME" \
  airflow-stable/airflow \
  --namespace "$AIRFLOW_NAMESPACE" \
  --version "8.6.0" \
  --values ./values.yaml


cp -r /root/systems/prod/airflow/dags/. /srv/nfs/kubedata/airflow-cluster-airflow-dags-pvc-pvc-fe2ddb07-8bb5-4a45-ba94-e2eaa5af9236

kubectl get pods -n <namespace> --no-headers=true | awk '/application/{print $1}'| xargs  kubectl delete -n <namespace> pod
