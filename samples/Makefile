#######################################
# Sample templates for fw-policy-test #
#######################################

KUBECTL := kubectl
CHECK_KUBECTL := $(shell which $(KUBECTL) | grep -c '[[:alnum:]]' )
K8_CRON_FILE := fw-policy-test.yaml
K8_CRON_PGW_FILE := fw-policy-test-pgw.yaml

.PHONY: help
help:
	@ echo "'make' options are:"
	@ echo " - make k8-cronjob: create a kubernetes cronjob"
	@ echo " - make k8-cronjob-pgw: create a kubernetes cronjob with push-gateway turned on"
	@ echo " - make clean-k8-cronjob: clean a kubernetes cronjob"
	@ echo " - make clean-k8-cronjob-pgw: clean a kubernetes cronjob that has push-gateway turned on"
	@ echo " - make list-k8-cronjob: list kubernetes cronjob"
	@ echo " - make check-kubectl: check if kubectl binary exists"
	
.PHONY: k8-cronjob
k8-cronjob: check-kubectl
	@ if [ -f "$(K8_CRON_FILE)" ]; then \
		echo "File: $(K8_CRON_FILE) exists" ;\
		$(KUBECTL) apply -f $(K8_CRON_FILE) ;\
	else \
		echo "File: $(K8_CRON_FILE) cannot be found" ;\
	fi

.PHONY: clean-k8-cronjob
clean-k8-cronjob: check-kubectl
	@ if [ -f "$(K8_CRON_FILE)" ]; then \
		echo "File: $(K8_CRON_FILE) exists" ;\
		$(KUBECTL) delete -f $(K8_CRON_FILE) ;\
	else \
		echo "File: $(K8_CRON_FILE) cannot be found" ;\
	fi

.PHONY: k8-cronjobi-pgw
k8-cronjob-pgw: check-kubectl
	@ if [ -f "$(K8_CRON_PGW_FILE)" ]; then \
		echo "File: $(K8_CRON_PGW_FILE) exists" ;\
		$(KUBECTL) apply -f $(K8_CRON_PGW_FILE) ;\
	else \
		echo "File: $(K8_CRON_PGW_FILE) cannot be found" ;\
	fi

.PHONY: clean-k8-cronjob-pgw
clean-k8-cronjob-pgw: check-kubectl
	@ if [ -f "$(K8_CRON_PGW_FILE)" ]; then \
		echo "File: $(K8_CRON_PGW_FILE) exists" ;\
		$(KUBECTL) delete -f $(K8_CRON_PGW_FILE) ;\
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
	@ echo "'$(KUBECTL)': Doesn't exist"
	@ exit 1
endif
	@ echo "'$(KUBECTL)': exists"
