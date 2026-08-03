
PROJECT := fw-policy-test
VERSION_TAG := 0.1
IMAGE_TAG = $(PROJECT)
DOCKER_IMAGE = $(IMAGE_TAG):$(VERSION_TAG)
IMAGE_EXISTS := $(shell docker image inspect $(DOCKER_IMAGE) > /dev/null 2>&1  ; echo $$? )

help:
	@echo "Usage 'make':"
	@echo "- make run-pytest: run $(PROJECT) as a pytest script run-time"
	@echo "- make run-docker: run $(PROJECT) as a docker image container"
	@echo "- make clean-docker: clean & remove docker image $(PROJECT)"
	@echo "- make create-docker: create docker image $(PROJECT)"

run-pytest:
	@echo "Running fw-policy-test as a pytest script"
	sudo pytest -v -s --tb=no

run-docker:
ifeq ($(IMAGE_EXISTS), 0)
	@echo "Docker image $(DOCKER_IMAGE) exists proceed with docker executions"
else
	@echo "Docker image $(DOCKER_IMAGE) does *NOT* exist proceed with docker creation"
	docker build -f Dockerfile -t $(DOCKER_IMAGE) .
endif
	@echo "Running fw-policy-test as a docker image: $(DOCKER_IMAGE)"
	@docker run -t $(DOCKER_IMAGE) || true

clean-docker:
	@echo "Cleaning up the following docker image tag: $(DOCKER_IMAGE)"
	@docker image rm -f $(DOCKER_IMAGE)

create-docker: Dockerfile
	@echo "Creating docker image file using the following image tag: $(DOCKER_IMAGE)"
	@docker build -f Dockerfile -t $(DOCKER_IMAGE) .
