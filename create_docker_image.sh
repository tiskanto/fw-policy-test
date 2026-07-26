#!/bin/sh
# Create fw-policy-test Docker image

# Docker vars
VERSION_TAG="0.1"
IMAGE_TAG="fw-policy-test"
DOCKER_IMAGE="${IMAGE_TAG}:${VERSION_TAG}"

# Docker creation
echo "Creating fw-policy-test with the following tag: $DOCKER_IMAGE"
docker build -f Dockerfile -t $DOCKER_IMAGE .
