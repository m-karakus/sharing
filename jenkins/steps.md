kubectl create namespace devops-tools
kubectl apply -f serviceAccount.yaml
kubectl apply -f service.yaml
kubectl apply -f volumeclaim.yaml
kubectl apply -f deployment.yaml


kubectl get deployments -n devops-tools
kubectl get pods --namespace=devops-tools

kubectl logs jenkins-b96f7764f-x294k --namespace=devops-tools
9d7b422bccad45a7bbb802591bf03c46