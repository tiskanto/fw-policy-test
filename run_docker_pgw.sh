#!/bin/sh

# Docker vars
VERSION_TAG="0.1"
IMAGE_TAG="fw-policy-test"
DOCKER_IMAGE="${IMAGE_TAG}:${VERSION_TAG}"

# Image ENV vars
ENV_PROM_PGW_HOST="192.168.0.223:9091"
ENV_PROM_PGW_ENABLED=1

# Running fw-policy-test Docker image with Prometheus push-gateway
docker run -e PROM_PGW_ENABLED=$ENV_PROM_PGW_ENABLED -e PROM_PGW_HOST=$ENV_PROM_PGW_HOST -t $DOCKER_IMAGE
