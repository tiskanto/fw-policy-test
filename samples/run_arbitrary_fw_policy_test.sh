#!/bin/sh
######################################
# Run arbitrary docker image via k8
######################################

# image without prometheus gateway (normal)
function run_normal() {
	kubectl run my-task \
	  --rm -it \
	  --image=fw-policy-test:0.1\
	  --overrides='
	{
	  "spec": {
	    "hostNetwork": true,
	    "containers": [
	      {
	        "name": "my-task",
	        "image": "fw-policy-test:0.1",
	        "imagePullPolicy": "Never",
	        "stdin": true,
	        "tty": true
	      }
	    ]
	  }
	}'
}

# image with prometheus push-gateways
function run_pgw() {
	kubectl run my-task \
	  --env="PROM_PGW_ENABLED=1" \
	  --env="PROM_PGW_HOST=${1}" \
	  --rm -it \
	  --image=fw-policy-test:0.1
}

# help function
function help() {
  echo "Running fw-policy-test docker image via kubernetes run"
  echo "Usage:"
  echo "- ${0} <enter>         : running k8 docker image without push-gateway support"
  echo "- ${0} -p <enter>      : running k8 docker image with default push-gateway setup"
  echo "- ${0} -p <node:port>> : running k8 docker image with non-default push-gateway setup"
  exit 0
}

# commandline args trap
if [ -z "${1}" ]; then
  echo "Run normal fw-policy-test without the Prometheus push-gateway support"
  run_normal
else
  if [ "${1}" == "-p" ]; then

    # default PGW setups
    PROM_PGW_HOST=${2:-"192.168.0.223:9091"}

    echo "Run fw-policy-test with the default Prometheus push-gateway setup"
    echo "PROM_PGW_HOST: ${PROM_PGW_HOST}"
    run_pgw ${PROM_PGW_HOST}

  else
    help
  fi
fi
