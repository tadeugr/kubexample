#!/usr/bin/env bash

# Send requests to kubexample Kubernetes service.

# Iterate from 1 to 100.
for i in {1..100}
do
    # Make a get request
    curl kubexample.kubexample.svc.cluster.local/payload;
    
    # Give it some time to breathe
    sleep 1
done
