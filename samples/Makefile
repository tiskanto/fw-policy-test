#######################################
# Sample templates for fw-policy-test #
#######################################

# Docker image vars
# Change the 'VERSION_TAG' according to the release version

PROJECT := fw-policy-test
VERSION_TAG := 0.2
DOCKER_IMAGE = $(PROJECT):$(VERSION_TAG)

# Prometheus push-gateway default vars
ENV_PROM_PGW_HOST ?= 127.0.0.1:9091
ENV_PROM_PGW_ENABLED ?= 0

# Kubectl vars
KUBECTL := kubectl
CHECK_KUBECTL := $(shell which $(KUBECTL) | grep -c '[[:alnum:]]' )
K8_CRON_FILE := fw-policy-test.yaml
K8_CRON_PGW_FILE := fw-policy-test-pgw.yaml

.PHONY: help
help:
	@ echo "'make' options are:"
	@ echo " - make k8-runjob: creates & executes kubernete job"
	@ echo " - make k8-runjob-pgw: creates & executes kubernete job with push-gateway"
	@ echo " - make k8-cronjob: create a kubernetes cronjob"
	@ echo " - make k8-cronjob-pgw: create a kubernetes cronjob with push-gateway"
	@ echo " - make clean-k8-cronjob: clean a kubernetes cronjob"
	@ echo " - make clean-k8-cronjob-pgw: clean a kubernetes cronjob that has push-gateway"
	@ echo " - make list-k8-cronjob: list kubernetes cronjob"
	@ echo " - make check-kubectl: check if kubectl binary exists"
	@ echo "+================================================================================+"
	@ echo "|    ** Use ENV_PROM_PGW_HOST=<pgw_host:pgw_port> (default:127.0.0.1:9091)       |"
	@ echo "|        e.g make k8-runjob-pgw ENV_PROM_PGW_HOST=<pgw_host:pgw_port>            |"
	@ echo "+================================================================================+"

.PHONY: k8-runjob
k8-runjob: check-kubectl
	@ echo "Running k8 job with docker image :$(DOCKER_IMAGE)"
	@ kubectl run fw-policy-test --rm -it --image=$(DOCKER_IMAGE)

.PHONY: k8-runjob-pgw
k8-runjob-pgw: check-kubectl
	@ echo "Running k8 prometheus support job with docker image :$(DOCKER_IMAGE)"
	@ kubectl run fw-policy-test-pgw --rm -it --image=$(DOCKER_IMAGE) \
	    --env="PROM_PGW_ENABLED=1" \
	    --env="PROM_PGW_HOST=$(ENV_PROM_PGW_HOST)"
	
.PHONY: k8-cronjob
k8-cronjob: check-kubectl
	@ if [ -f "$(K8_CRON_FILE)" ]; then \
		echo "File: $(K8_CRON_FILE) exists" ;\
		export PROJECT=$(PROJECT) ; \
		export DOCKER_IMAGE=$(DOCKER_IMAGE) ; \
		envsubst < $(K8_CRON_FILE) | $(KUBECTL) apply -f - ;\
	else \
		echo "File: $(K8_CRON_FILE) cannot be found" ;\
	fi

.PHONY: clean-k8-cronjob
clean-k8-cronjob: check-kubectl
	@ if [ -f "$(K8_CRON_FILE)" ]; then \
		echo "File: $(K8_CRON_FILE) exists" ;\
		export PROJECT=$(PROJECT) ; \
		export DOCKER_IMAGE=$(DOCKER_IMAGE) ; \
		envsubst < $(K8_CRON_FILE) | $(KUBECTL) delete -f - ;\
	else \
		echo "File: $(K8_CRON_FILE) cannot be found" ;\
	fi

.PHONY: k8-cronjobi-pgw
k8-cronjob-pgw: check-kubectl
	@ if [ -f "$(K8_CRON_PGW_FILE)" ]; then \
		echo "File: $(K8_CRON_PGW_FILE) exists" ;\
		export PROJECT=$(PROJECT) ; \
		export DOCKER_IMAGE=$(DOCKER_IMAGE) ; \
		envsubst < $(K8_CRON_PGW_FILE) | $(KUBECTL) apply -f - ;\
	else \
		echo "File: $(K8_CRON_PGW_FILE) cannot be found" ;\
	fi

.PHONY: clean-k8-cronjob-pgw
clean-k8-cronjob-pgw: check-kubectl
	@ if [ -f "$(K8_CRON_PGW_FILE)" ]; then \
		echo "File: $(K8_CRON_PGW_FILE) exists" ;\
		export PROJECT=$(PROJECT) ; \
		export DOCKER_IMAGE=$(DOCKER_IMAGE) ; \
		envsubst < $(K8_CRON_PGW_FILE) | $(KUBECTL) delete -f - ;\
	else \
		echo "File: $(K8_CRON_PGW_FILE) cannot be found" ;\
	fi

.PHONY: list-k8-cronjob
list-k8-cronjob: check-kubectl
	@ echo "List k8 cronjob"
	@ $(KUBECTL) get cronjob -A

.PHONY: check-kubectl
check-kubectl:
ifeq ($(CHECK_KUBECTL), 0)
	@ echo "['$(KUBECTL)': Doesn't exist] ❌"
	@ exit 1
endif
	@ echo "['$(KUBECTL)': exists] ✅"
