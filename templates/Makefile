#######################################
# Sample templates for fw-policy-test #
#######################################

KUBECTL := kubectl
CHECK_KUBECTL := $(shell which $(KUBECTL) | grep -c '[[:alnum:]]' )

K8_CRON_FILE := fw-policy-test.yaml
K8_CRON_PGW_FILE := fw-policy-test-pgw.yaml

.PHONY: k8-cronjob
k8-cronjob: check-kubectl
	@ if [ -f "$(K8_CRON_FILE)" ]; then \
		echo "$(K8_CRON_FILE) exists" ;\
		echo "line2 exists" ;\
		$(KUBECTL) apply -f $(K8_CRON_FILE) ;\
	else \
		echo "$(K8_CRON_FILE) cannot be found" ;\
		echo "line2 for cannot be found exists" ;\
	fi

clean-k8-cronjob: check-kubectl
	@ if [ -f "$(K8_CRON_FILE)" ]; then \
		echo "$(K8_CRON_FILE) exists" ;\
		echo "line2 exists" ;\
		$(KUBECTL) delete -f $(K8_CRON_FILE) ;\
	else \
		echo "$(K8_CRON_FILE) cannot be found" ;\
		echo "line2 for cannot be found exists" ;\
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
