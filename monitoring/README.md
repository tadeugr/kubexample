# Deploy monitoring stack

Install Prometheus and Grafana in `monitoring` namespace by running:

```bash
make install
```

# Access Prometheus

Create Prometheus port forwarding:

```bash
make fw-prom
```

> Leave the command running to keep the port open.

Then access in your web browser: http://localhost:9090

# Access Grafana

Create Grafana port forwarding:

```bash
make fw-grafana
```

> Leave the command running to keep the port open.

Then access in your web browser: http://localhost:3000

The user is `admin` and you can get the password by running:

```bash
make get-grafana-secret
```

## Import kubexample dashboard

Copy the contets of `kubexample-dashboad.json`.

Go to `Dashboards`, `New`, `Import` and paste the `json` in `Import via dashboard JSON model`.

Click on `Load`.

# Trobouleshoot

## servicemonitor not being discovered

https://github.com/prometheus-operator/kube-prometheus/issues/1392