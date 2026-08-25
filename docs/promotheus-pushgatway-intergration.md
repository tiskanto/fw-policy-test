# `fw-policy-test` with Promotheus and Pushgateway Integration

## Table of Contents
- [Promotheus Pushgateway Intergration Benefits](#promotheus-pushgateway-integration-benefits)
- [How It Works](#how-it-works)
- [Requirements](#requirements)
- [Integration Steps](#integration-steps)

## Promotheus pushgateway integration benefits
- `fw-policy-test` metrics can be easily calculated, processed and charted
- With the use of `PromQL` data can be easily filtered & massaged for further processing
- Prometheus should be able to perform alarming using the alert-manager & furthermore integrated into PagerDuty
- Further integration with Prometheus and Grafana is also possible

## How it works
Please look at the following diagram for details:
```

(*) fw-policy-test
+-----------------------+
| - dockerized apps     |
| - native pytest apps  |
| - kubernetes cron     |
| - kubernetes job      |
+-----------------------+
           |
           V
+----------------------+    +------------- +    +----------------------+    +---------------+
|                      |    |              |    |                      |    |               |
| ephemeral jobs/batch |--->| Pushgateway  |<---| Prometheus Server(s) |--->| Grafana/Graph |
|                      |    |              |    | **metrics  scraping  |    |   Dashboard   |
+----------------------+    +------------- +    +----------------------+    +---------------+
                                   |
                                   V
                            +------------- +    +------------- +    +------------- +
                            |              |    |              |    |  - Slack     |
                            | Alertmanager |--->| Notification |--->|  - PagerDuty |
                            |              |    |    Rcvd's    |    |  - MSTeams   |
                            +------------- +    +------------- +    +--------------+
```
Note:
- `pushgateway` can be running on a localhost or on a remotehost (please ensure the ports are unique when running as local)
- `prometheus` ideally has to be running on a separate host as it will require logs and data storage
- `grafana` is external third party tools where user(s) can create dashboard based on the ingested metrics received
- `alertmanager` is another component within prometheus where it can trigger alarm based on a configured breach threshold

## Requirements
- At the very least a `pushgateway` and a `prometheus` is required
- Having an `alertmanager` and `grafana` are optional

## Integration Steps
Following are the steps that can be followed to perform integration with `pushgateway` and `prometheus`

#### Step1:
On your localhost where you want to run your application, edit [fw-policy-test-pgw.yaml](samples/fw-policy-test-pgw.yaml) from the [samples](samples) folder. Adjust the cronjob `schedule` frequency time and your `PROM_PGW_HOST`

```
apiVersion: batch/v1
kind: CronJob
metadata:
  name: fw-policy-test-pgw-v1
  labels:
    app: fw-policy-test-pgw-v1
spec:
  schedule: "*/5 * * * *" ------------> !
  jobTemplate:
    spec:

--- SNIP ---

  terminationMessagePath: /var/log/fw-policy-test.log
  stdin: true
  tty: true
  env:
    - name: PROM_PGW_ENABLED
      value: "1"
    - name: PROM_PGW_HOST
      value: "192.168.0.223:9091" ----------> !
restartPolicy: Never

```

#### Step2:
Once the above file has been updated & saved reflecting to your infrastructure environment, then perform the following from [samples](samples) folder on your localhost where you host the application

```
shell> make
'make' options are:
 - make k8-cronjob: create a kubernetes cronjob
 - make k8-cronjob-pgw: create a kubernetes cronjob with push-gateway turned on
 - make clean-k8-cronjob: clean a kubernetes cronjob
 - make clean-k8-cronjob-pgw: clean a kubernetes cronjob that has push-gateway turned on
 - make list-k8-cronjob: list kubernetes cronjob
 - make check-kubectl: check if kubectl binary exists
```

```
# To install the k8-cronjob with Pushgateway support
shell> make k8-cronjob-pgw

# To list the newly installed k8-cronjob that has Pushgateway support
shell> make list-k8-cronjob-pgw

# To clean / remove existing k8-cronjob
shell> make clean-k8-cronjob-pgw
```

#### Step3:
Go into your remote host where you want to install & run `prometheus` and `pushgateway`. Please ensure that docker is installed and perform the copy of the [prometheus_pgw](samples/prometheus_pgw). Once copied, run the shell script with the following command:
```
shell> ./run_docker_compose.sh
Perform Docker Compose Function(s)
Usage:
- ./run_docker_compose.sh -u: docker-compose up
- ./run_docker_compose.sh -d: docker-compose down
- ./run_docker_compose.sh -l: docker-compose logs
- ./run_docker_compose.sh -s: docker-compose stats
```

To start-up `prometheus` and `pushgateway`:
```
# to start
shell> ./run_docker_compose,sh -u

# to stop
shell> ./run_docker_compose,sh -d

# to monitor/check the logs
shell> ./run_docker_compose,sh -l

# to check the stats
shell> ./run_docker_compose,sh -s
```

#### Step4:
Please ensure that the `k8-cronjob` is running (you can do this with `make list-k8-cronjob` and the `prometheus` and `pushgateway` is running (you can do this with `./run_docker_compose.sh -l` -or- `./run_docker_compose.sh -s`).


#### End
