# Apply all yaml files in this folder
apply:
	kubectl apply -f "*.yaml"

# Delete kubernetes resources in all yaml files in this folder
delete:
	kubectl delete -f "*.yaml"

# Create port forwarding to kubexample service
fw-kubexample:
	kubectl port-forward svc/kubexample 8080:80 -n kubexample

# Allocate a tty to a kubexample pod
pod-tty:
	kubectl -n kubexample exec --stdin --tty deployment/kubexample -- /bin/bash

# Force deployment rollout to test HA
force-rollout:
	kubectl rollout restart deployment/kubexample -n kubexample