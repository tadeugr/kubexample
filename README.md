`kubexample` is a simple Python/Flask microservice being packed into a docker image and deployed to Kubernetes to showcase some basic DevOps principles.

# Before you begin

This project has been built and extensively tested using [UTM Ubuntu 22.04 ARM64](https://mac.getutm.app/gallery/ubuntu-20-04) guest Virtual Machine on a MacBook M1 host.

Most tools and commands used here are configured to be architecture agnostic, although be aware some small deviations might occur if you are using a different setup.

If you wish to use the very same environment, please follow [this documentation](./doc/utm-ubuntu-2204-arm64.md).

# Requirements

The following tools are required to build and run this project.

- `git`

- `Python 3.10.12`