`kubexample` is a simple Python/Flask microservice being packed into a docker image and deployed to Kubernetes to showcase some basic DevOps principles.

# Folder structure

```
├── README.md                    This file.
├── app                          Microservice Docker and source code.
│   ├── Dockerfile               Multi-stage Docker file.
│   ├── Makefile                 Commands to manage docker.
│   ├── requirements.txt         Microservice Python requirements.
│   └── src                      Microservice source code.
│       ├── Makefile             Commands to manage the application.
│       ├── benchmark.sh         Test the application from inside a Kubernetes pod.
│       ├── kubexample.py        Flask server main file.
│       └── wsgi.py              Gunicorn Web Server Gateway Interface.
├── dist                         Kubernetes manifests to deliver the application.
│   ├── Makefile                 Commands to install and uninstall the application.
│   ├── aux.yaml                 Auxiliary deployment (to run the benchmark).
│   └── kubexample.yaml          Microservice deployment.
├── doc
│   └── utm-ubuntu-2204-arm64.md Documentation to install a lab VM.
├── kind                         Kubernetes kind configuration.
│   ├── Makefile                 Commands to create and delete a cluster.
│   ├── README.md                Kind documentation.
│   └── kind.yaml                Kind multi-node configuration.
└── monitoring                   Prometheus/Grafana files.
    ├── Makefile                 Commands to install monitoring stack.
    ├── README.md                Monitoring documentation.
    ├── kubexample-dashboad.json Microservice Grafana dashboard.
    └── values.yml               Prometheus helm values.
```

# Before you begin

This project has been built and extensively tested using [UTM Ubuntu 22.04 ARM64](https://mac.getutm.app/gallery/ubuntu-20-04) guest Virtual Machine on a MacBook M1 host.

Most tools and commands used here are configured to be architecture agnostic, although be aware some small deviations might occur if you are using a different setup.

If you wish to use the very same environment, please follow [this documentation](./doc/utm-ubuntu-2204-arm64.md).

> **WARNING** All `cd` commands in this documentation are relative to the project root folder, so make sure are in the correct directory.

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
# pwd is <project root folder>/app
make requirements
```

Start the application:

```bash
cd app/src
# pwd is <project root folder>/app/src
make start-dev
```

You should see somehting like this:

```
* Serving Flask app 'kubexample'
 * Debug mode: off
[2024-07-28 11:46:50]: 38007 INFO WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.64.4:5000
[2024-07-28 11:46:50]: 38007 INFO Press CTRL+C to quit

```

Leave the process running, and access http://127.0.0.1:5000 in your web browser. You should see the application home page `Hello, home!`.

Terminate the process running in your terminal by pressing `CTRL + C`.

# Setup docker image

Go to `app` folder.

```bash
cd app
# pwd is <project root folder>/app
```

## Build image

```bash
make build
```

Smoke test the image by running:

```bash
make docker-run-start
```

You should see something like this:

```
[2024-07-28 11:51:28 +0000] [7] [INFO] Starting gunicorn 20.1.0
[2024-07-28 11:51:28 +0000] [7] [DEBUG] Arbiter booted
[2024-07-28 11:51:28 +0000] [7] [INFO] Listening at: http://0.0.0.0:5000 (7)
[2024-07-28 11:51:28 +0000] [7] [INFO] Using worker: sync
[2024-07-28 11:51:28 +0000] [8] [INFO] Booting worker with pid: 8
[2024-07-28 11:51:28 +0000] [7] [DEBUG] 1 workers
```

> Leave the command above running.

Access http://127.0.0.1:5000 in your web browser, you should see the home page again.

Terminate the running command by pressing `CTRL + C` in your terminal. 

If by any chance you need to troubleshoot the application in the container, you can do this:

```
make docker-run-bash
# Then, from inside the container, run:
make start-dev
# To exit press CTRL + D or run exit command
```

> `make start-dev` starts Flask dev server. If you need to test the application using the production web server (`gunicorn`), run `make start`.

## "Push" image

> This is a dummy application running in a local cluster, so we are not using a proper Docker Registry, luckily kind has a built tool to push the image to all Kubernetes nodes..

Make the image available in `kind` by running:

```bash
make push
```

You should see somehting like this:

```
kind load docker-image kubexample:v1
Image: "kubexample:v1" with ID "sha256:737163ad02fe8f96f7abd7cfc3fb5f40f53dc9b8983be50251f6edf309fbac97" not yet present on node "kind-control-plane", loading...
Image: "kubexample:v1" with ID "sha256:737163ad02fe8f96f7abd7cfc3fb5f40f53dc9b8983be50251f6edf309fbac97" not yet present on node "kind-worker", loading...
Image: "kubexample:v1" with ID "sha256:737163ad02fe8f96f7abd7cfc3fb5f40f53dc9b8983be50251f6edf309fbac97" not yet present on node "kind-worker2", loading...
Image: "kubexample:v1" with ID "sha256:737163ad02fe8f96f7abd7cfc3fb5f40f53dc9b8983be50251f6edf309fbac97" not yet present on node "kind-worker3", loading...
```

> **Congrats!** Everything is ready to start the deploying the application.

## Deploy monitoring stack

Follow the instructions in [Monitoring Documentation](./monitoring/README.md)

## Deploy application

```bash
cd dist
# pwd is <project root folder>/dist
make apply
```
> If for any reason you need to delete (uninstall) the application in the future, run `make delete`.

To access the application, create a port forward (leave the process running):

```bash
# pwd is <project root folder>/dist
make fw-kubexample
```

You should see something like this:

```
Forwarding from 127.0.0.1:8080 -> 5000
Forwarding from [::1]:8080 -> 5000
```

Then access in your web browser: http://localhost:8080/payload

You should see a `json` with the result.

> **Congrats!** At this point the entire stack is up and running and you can start playing around with it!

> **WARNING** the command above runs `kubectl port-forward`, and its default behaviour is to select and connect to a single Kubernetes service endpoint, which means it does not use Kubernetes Service Round Robin Load Balancer. So be aware port fowarding is **NOT** suitable for spreading requests across all pods. To do so, follow the instructions bellow.

You may exit the application port forward in your terminal if you don't want to access it from your browser anymore.

# Load Balance requests

Connect to the auxiliary pod terminal by running:

```bash
cd dist/
# pwd is <project root folder>/dist
make aux-tty
```

Then, from inside the pod, run:

```bash
./benchmark.sh
```

> **Why all this?** This is the closest we can get to a production environment regarding Load Balancing. Since we are not running Kubernetes on the cloud (nor using MetalLB), there is no Kubernetes service `type: LoadBalancer`. luckily any Kubernetes service supports under the hood a very basic Round Robin Load Balancing, we are just making sure we are using a Kubernetes service FQDN.

> **Why not to use an ingress?** To keep it simple at this moment, for the purpose of this project introducing one more layer of complexity could be an overkill. Although, setting up `nginx` is planned as an enhancement in the project [Roadmap](#roadmap).

Now if go to Grafana you should see metrics being populated.

# Roadmap

- Make developers' life easier by implementing Continuous Development

  - `Phase 01`: implement `docker-compose`;

  - `Phase 02`: implement https://tilt.dev/

- Make image tag dynamic. Right now it is hardcoded `kubexample:v1`;

- Create different environment configurations. At this moment the webserver port is hardcoded `5000` and debug logging is enabled. You might want something different when going to a real production environment.

- Setup and use Docker Registry.

- Consider adding `nginx` ingress.

- Automatically create Grafana dashboard.