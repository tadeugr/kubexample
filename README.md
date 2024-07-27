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

- `kind` and an up and running local cluster;

- `kubectl`;

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
docker run --rm -it -p 5000:5000 kubexample:v1
```

If by any chance you need to troubleshoot the application in the container, you can do this:

```
docker run --rm -it --entrypoint "/bin/bash" kubexample:v1
make start-dev
```

## "Push" image

> This is a dummy application running in a local cluster, so we are not using a Docker Registry.

Make the image available in `kind`:

```bash
make push
```

# Roadmap

- Make developers' life easier by implementing Continuous Development

  - `Phase 01`: implement `docker-compose`;

  - `Phase 02`: implement https://tilt.dev/

- Make image tag dynamic. Right now it is hardcoded `kubexample:v1`;

- Create different environment configurations. At this moment the webserver port is hardcoded `5000` and debug logging is enabled. You might want something different when going to a real production environment.

- Setup and use Docker Registry.

# References

## Docker 201: Multi-Stage Builds for Production

https://medium.com/@ketangangal98/docker-201-multi-stage-builds-for-production-59b1ea98924a

https://github.com/rycus86/prometheus_flask_exporter/tree/master

https://github.com/jonashaag/prometheus-multiprocessing-example/tree/master

https://kubernetes.github.io/ingress-nginx/user-guide/monitoring/#prometheus-and-grafana-installation-using-service-monitors

https://www.aviator.co/blog/how-to-monitor-and-alert-on-nginx-ingress-in-kubernetes/