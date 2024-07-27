# Monitoring

helm install kube-prometheus-stack prometheus-community/kube-prometheus-stack --create-namespace -n monitoring  --values values.yml

helm upgrade kube-prometheus-stack prometheus-community/kube-prometheus-stack --namespace monitoring --values values.yml

kubectl get secret kube-prometheus-stack-grafana -o jsonpath="{.data.admin-password}"  -n monitoring | base64 --decode ; echo

kubectl port-forward svc/kube-prometheus-stack-prometheus 9090:9090 -n monitoring
kubectl port-forward svc/kube-prometheus-stack-grafana 3000:80 -n monitoring

# Trobouleshoot

## servicemonitor not being discovered

https://github.com/prometheus-operator/kube-prometheus/issues/1392