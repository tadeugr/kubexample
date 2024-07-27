# Install kube-prometheus-stack
install:
	helm install kube-prometheus-stack prometheus-community/kube-prometheus-stack --create-namespace -n monitoring  --values values.yml

# Upgrade current kube-prometheus-stack instalation
upgrade:
	helm upgrade kube-prometheus-stack prometheus-community/kube-prometheus-stack --namespace monitoring --values values.yml

# Get grafana admin user password
get-grafana-secret:
	kubectl get secret kube-prometheus-stack-grafana -o jsonpath="{.data.admin-password}"  -n monitoring | base64 --decode ; echo

# Create prometheus port foward
fw-prom:
	kubectl port-forward svc/kube-prometheus-stack-prometheus 9090:9090 -n monitoring

# Create grafana port forward
fw-grafana:
	kubectl port-forward svc/kube-prometheus-stack-grafana 3000:80 -n monitoring