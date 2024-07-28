#!/usr/bin/env bash

# Send requests to kubexample Kubernetes service.

# Define curl format for debugging
CURL_FORMAT="/tmp/curl-format.txt"
cat <<EOT >> $CURL_FORMAT
     time_namelookup:  %{time_namelookup}s\n
        time_connect:  %{time_connect}s\n
     time_appconnect:  %{time_appconnect}s\n
    time_pretransfer:  %{time_pretransfer}s\n
       time_redirect:  %{time_redirect}s\n
  time_starttransfer:  %{time_starttransfer}s\n
                     ----------\n
          time_total:  %{time_total}s\n
EOT

# Iterate from 1 to 100.
for i in {1..100}
do
    echo "----------------------"

    # Make a get request
    curl -w "@$CURL_FORMAT" -o /dev/null -s "kubexample.kubexample.svc.cluster.local/payload"
    
    # Wait a bit
    sleep 1
done
