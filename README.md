`kubexample` is a simple Python/Flask microservice being packed into a docker image and deployed to Kubernetes to showcase some basic DevOps principles.

# Before you begin

This project has been built and extensively tested using [UTM Ubuntu 22.04 ARM64](https://mac.getutm.app/gallery/ubuntu-20-04) guest Virtual Machine on a MacBook M1 host.

Most tools and commands used here are configured to be architecture agnostic, although be aware some small deviations might occur if you are using a different setup.

If you wish to use the very same environment, please follow [this documentation](./doc/utm-ubuntu-2204-arm64.md).

# Requirements

The following tools are required to build and run this project.

- `git`;

- `Python 3.10.12` (and `python3-pip`);

- `make`;

- `docker`;

- `kind` and an up and running local cluster ([reference](./kind/README.md));

- `kubectl`;

- `helm 3`;

- `k9s` (optional);

# Run the application locally (optional)

Before we go to Docker and Kubernetes, run the application locally to check if everything is OK.

Go to `app` folder:

```bash
cd app
```

Install Python requirements by running:

```bash
pip3 install -r requirements.txt
```

Start the application:

```bash
make start
```

You should see somehting like this:

```
Running on http://127.0.0.1:5000
```

Leave the process running, and access http://127.0.0.1:5000 in your web browser. You should see the application home page.

You may now terminate the process running in your terminal by pressing `CTRL + C`.

# Setup docker image

## Build image

```bash
make build
```

Smoke test the image by running:

```bash
cd app
make docker-run-start
```

> Leave the command above running.

If by any chance you need to troubleshoot the application in the container, you can do this:

```
cd app
make docker-run-bash
# Then from inside the container, run:
make start-dev
```

## "Push" image

> This is a dummy application running in a local cluster, so we are not using a Docker Registry.

Make the image available in `kind`:

```bash
make push
```

## Deploy monitoring stack

Follow the instructions in [Monitoring Documentation](./monitoring/README.md)

## Deploy application

```bash
cd dist
make appy
```
> If you need to delete the application, run `make delete`

To access the application, create a port forward (leave the process running):

```bash
make fw-kubexample
```

Then access in your web browser: http://localhost:8080/payload 

> **WARNING** the command above runs `kubectl port-forward`, and its default behaviour is to select and connect to an endpoint, which means it does not use Kubernetes Service Round Robin Load Balancer. So be aware port fowarding is suitable for spreading requests across all pods. To do so follow the instructions bellow.

# Load Balance 100 requests

Connect to a pod terminal by running:

```bash
cd dist/
make pod-tty
```

Then, from inside the pod, run:

```bash
./benchmark.sh
```

> **Why all this?** This is the closest we can get to a production environment. Since we are not running Kubernetes on the cloud (nor using MetalLB), there is no Kubernetes service `type: LoadBalancer`. Luckly any Kubernetes service supports under the hood a very basic Round Robin load balancing, we are just making sure we reach Kubernetes service FQDN.

# Roadmap

- Make developers' life easier by implementing Continuous Development

  - `Phase 01`: implement `docker-compose`;

  - `Phase 02`: implement https://tilt.dev/

- Make image tag dynamic. Right now it is hardcoded `kubexample:v1`;

- Create different environment configurations. At this moment the webserver port is hardcoded `5000` and debug logging is enabled. You might want something different when going to a real production environment.

- Setup and use Docker Registry.

- Consider adding `nginx` ingress.

# References

## Docker 201: Multi-Stage Builds for Production

https://medium.com/@ketangangal98/docker-201-multi-stage-builds-for-production-59b1ea98924a

https://github.com/rycus86/prometheus_flask_exporter/tree/master

https://github.com/jonashaag/prometheus-multiprocessing-example/tree/master

https://kubernetes.github.io/ingress-nginx/user-guide/monitoring/#prometheus-and-grafana-installation-using-service-monitors

https://www.aviator.co/blog/how-to-monitor-and-alert-on-nginx-ingress-in-kubernetes/



https://pypi.org/project/prometheus-flask-exporter/

https://stackoverflow.com/questions/77145578/configuration-for-kubernetes-flask-and-prometheus

https://blog.viktoradam.net/2020/05/11/prometheus-flask-exporter/

https://medium.com/devops-techable/export-metrics-from-your-python-flask-application-to-prometheus-in-kubernetes-and-watch-your-9d45164f7adc

https://github.com/rycus86/prometheus_flask_exporter/blob/master/examples/sample-signals/grafana/dashboards/example.json