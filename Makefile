###################################
# fw-policy-test Makefile targets #
###################################

# Docker image vars
PROJECT := fw-policy-test
VERSION_TAG := 0.1
IMAGE_TAG = $(PROJECT)
DOCKER_IMAGE = $(IMAGE_TAG):$(VERSION_TAG)
IMAGE_EXISTS := $(shell docker image inspect $(DOCKER_IMAGE) > /dev/null 2>&1  ; echo $$? )

# Prometheus push-gateway default vars
ENV_PROM_PGW_HOST ?= 127.0.0.1:9091
ENV_PROM_PGW_ENABLED ?= 0

.PHONY: help
help:
	@echo "'make' options are:"
	@echo "- make run-pytest: run $(PROJECT) as a pytest script run-time"
	@echo "- make run-docker: run $(PROJECT) as a docker image container"
	@echo "- make run-docker-pgw: run $(PROJECT) as a docker image container with prometheus push-gateway support"
	@echo "- make clean-docker: clean & remove docker image $(PROJECT)"
	@echo "- make create-docker: create docker image $(PROJECT)"
	@echo "- make test-function: performs basic python module function calls"
	@echo "** Use ENV_PROM_PGW_HOST=<pgw_host:pgw_port> for prometheus push-gateway"

.PHONY: run-pytest
run-pytest:
	@echo "Running fw-policy-test as a pytest script"
	sudo pytest -v -s --tb=no

.PHONY: run-docker
run-docker:
ifeq ($(IMAGE_EXISTS), 0)
	@echo "Docker image $(DOCKER_IMAGE) exists proceed with docker executions"
else
	@echo "Docker image $(DOCKER_IMAGE) does *NOT* exist proceed with docker creation"
	@$(MAKE) create-docker
endif
	@echo "Running fw-policy-test as a docker image: $(DOCKER_IMAGE)"
	@docker run -t $(DOCKER_IMAGE) || true

.PHONY: run-docker-pgw
run-docker-pgw:
ifeq ($(IMAGE_EXISTS), 0)
	@echo "Docker image $(DOCKER_IMAGE) exists proceed with docker executions"
else
	@echo "Docker image $(DOCKER_IMAGE) does *NOT* exist proceed with docker creation"
	@$(MAKE) create-docker
endif
	@echo "Running fw-policy-test as a docker image: $(DOCKER_IMAGE)"
	@echo "With prometheus push-gateway: $(ENV_PROM_PGW_HOST)"
	@docker run -e PROM_PGW_ENABLED=1 -e PROM_PGW_HOST=$(ENV_PROM_PGW_HOST) -t $(DOCKER_IMAGE)

.PHONY: clean-docker
clean-docker:
	@echo "Cleaning up the following docker image tag: $(DOCKER_IMAGE)"
	@docker image rm -f $(DOCKER_IMAGE)

.PHONY: create-docker
create-docker: Dockerfile
	@echo "Creating docker image file using the following image tag: $(DOCKER_IMAGE)"
	@docker build -f Dockerfile -t $(DOCKER_IMAGE) .

.PHONY: test-function
test-function:
	@echo "Testing core function"
	@sudo python3 -m tests.function_check

