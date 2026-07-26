#!/bin/sh
# Executing fw-policy-test via docker image

# Docker vars
VERSION_TAG="0.1"
IMAGE_TAG="fw-policy-test"
DOCKER_IMAGE="${IMAGE_TAG}:${VERSION_TAG}"

# Running docker image
echo "Running fw-policy-test Docker image the following tag: $DOCKER_IMAGE"
docker run -t $DOCKER_IMAGE
