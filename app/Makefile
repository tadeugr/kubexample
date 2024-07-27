.PHONY: build
build:
	docker build -t kubexample:v1 .

push:
	kind load docker-image kubexample:v1

docker-run-start:
	docker run --rm -it -p 5000:5000 kubexample:v1

docker-run-bash:
	docker run --rm -it -p 5000:5000 --entrypoint "/bin/bash" kubexample:v1