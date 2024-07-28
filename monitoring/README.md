# Deploy monitoring stack

Make sure you are in this project folder:

```bash
cd monitoring/
# pwd is <project root folder>/monitoring
```

Add `kube-prometheus-stack` helm repo by running:

```bash
make repo-add
```

You should see somehting like this:

```
Hang tight while we grab the latest from your chart repositories...
...Successfully got an update from the "prometheus-community" chart repository
```

Install Prometheus and Grafana in `monitoring` namespace by running:

```bash
make install
```

You should see something like this:

```
kube-prometheus-stack has been installed. Check its status by running:
  kubectl --namespace monitoring get pods -l "release=kube-prometheus-stack"

Visit https://github.com/prometheus-operator/kube-prometheus for instructions on how to create & configure Alertmanager and Prometheus instances using the Operator.
```

# Access Prometheus

Create Prometheus port forwarding:

```bash
make fw-prom
```

You should see something like this:

```
Forwarding from 127.0.0.1:9090 -> 9090
Forwarding from [::1]:9090 -> 9090
```

> Leave the command running to keep the port open.

Then access in your web browser: http://localhost:9090

# Access Grafana

> You will need to keep few terminal windows open, you may use tmux if you want.

Create Grafana port forwarding:

```bash
make fw-grafana
```

You should see something like this:

```
Forwarding from 127.0.0.1:3000 -> 3000
Forwarding from [::1]:3000 -> 3000
```

> Leave the command running to keep the port open.

Then access in your web browser: http://localhost:3000

The user is `admin` and you can get the password by running this in another terminal:

```bash
make get-grafana-secret
```

The password is the string right after this:

```
kubectl get secret kube-prometheus-stack-grafana -o jsonpath="{.data.admin-password}"  -n monitoring | base64 --decode ; echo
```

## Import kubexample dashboard

Copy the contets of `kubexample-dashboad.json`.

Go to `Dashboards` (left side menu, you may need to click the hamburger menu to expand it), `New` (top-right corner, a blue button), `Import` and paste the `json` in `Import via dashboard JSON model`.

Click on `Load`, then on `Import`.

> For now the dashboard will show `No Data` because the application is not running yet, thus it is not generating metrics. You may now to back to [Deploy application](https://github.com/tadeugr/kubexample?tab=readme-ov-file#deploy-application).

# Trobouleshoot

## servicemonitor not being discovered

https://github.com/prometheus-operator/kube-prometheus/issues/1392