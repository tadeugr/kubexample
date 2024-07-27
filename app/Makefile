# Install python requirements
requirements:
	pip3 install -r requirements.txt

# Build docker image
build:
	docker build -t kubexample:v1 .

# "Push" images to kind nodes
push:
	kind load docker-image kubexample:v1

# Run kubexample docker container with default entrypoint
docker-run-start:
	docker run --rm -it -p 5000:5000 kubexample:v1

# Run kubexample docker container in bash mode
docker-run-bash:
	docker run --rm -it -p 5000:5000 --entrypoint "/bin/bash" kubexample:v1