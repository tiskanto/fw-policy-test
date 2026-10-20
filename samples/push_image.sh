#!/bin/zsh
# Note: change the version tag according to the version release
PROJECT=fw-policy-test
VERSION_TAG=0.2
DOCKER_VERSION=${PROJECT}:${VERSION_TAG}
sudo -E /usr/local/bin/minikube image load $DOCKER_VERSION
