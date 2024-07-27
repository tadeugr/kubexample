# Build Stage
FROM python:3.10-slim AS build 
RUN apt-get update && apt-get -y install libpq-dev gcc
COPY ./requirements.txt requirements.txt
RUN pip3 install --no-cache-dir --target=packages -r requirements.txt

# Runtime Stage
FROM python:3.10-slim AS runtime
RUN apt-get update && apt-get install -y curl build-essential gunicorn 
COPY --from=build packages /usr/lib/python3.10/site-packages
ENV PYTHONPATH=/usr/lib/python3.10/site-packages

# Security Context 
RUN useradd -m nonroot
USER nonroot

# Env configuration
WORKDIR /app
COPY ./src /app
ENTRYPOINT ["make","start"]