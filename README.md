# fw-policy-test

## Table of Contents
- [What](#what)
- [Why](#why)
- [Use Case](#use-cases)
- [Features](#features)
- [Design Concept](#design-concept)
- [Test Case File](#test-case-file)
  - [Sample Test Case](#sample-test-case)
  - [Test Case Format](#test-case-format)
- [Running the Application](#running-the-application)
---

## What:
`fw-policy-test` is a `pytest` native tool that can perform firewall policy verification against target hosts for compliance purposes.

`fw-policy-test` tool can be dynamically configured based on test scenarios and can be run natively via `pytest` or as a `docker` image container application. Since it can be run as a containerized application, it can be executed as a `k8 cronjobs`.

Also for observability purpose it can also be integrated with `prometheus` and `push-gateways`

## Why:
The idea is to ensure that, through a set of tests against target hosts (this could be a positive test or negative test) a compliance verification of firewall policies can be ascertained and verified.

## Use cases:
- Firewall policy verification tool
- Compliance test & verification tool
- Ensuring a policy is actively running against a target host/hosts
- Audit verification tool on perimeter security policy

## Features:
- Native `pytest` & `python3` application
- Containerized friendly and can be run as a `docker` image
- Can be run in `kubernetes` as a `k8 cronjob` or as an arbitrary application in `k8 job`
- Extensible modules (future feature)

## Design concept:
Please find the following diagram for the architectural design of `fw-policy-test`

![diagram](docs/pics/fw-policy-test-diagram.png)

## Test case file:
The test case file is in `YAML` format and the test case should reflect on what tests need to be performed and the expected test results from the target host(s). 

### Sample test case:
```
---
- hostname: Linux System A
  ip_addr: 192.168.0.181
  test_set:
    - name: tcp_one
      desc: testing SSH port
      proto: tcp
      port: 22
      expected: 1
    - name: tcp_two
      desc: testing dummy TCP port
      proto: tcp
      port: 2222
      expected: 0

     --- SNIP ---

- hostname: Linux System B
  ip_addr: 192.168.0.191
  test_set:
    - name: icmp_one
      desc: testing ICMP echo
      proto: icmp
      port: 0
      expected: 0
- hostname: Linux System C
  ip_addr: 192.168.17.221
  test_set:
    - name: icmp one
      desc: testing icmp
      proto: icmp
      port: 0
      expected: 1
```

### Test case format:

| **Attribute name** | **Type** | **Description** |
| --- | --- | --- |
| hostname | string | hostname description |
| ip_addr | string | IP address of the target host |
| name | string | name of the protocol / test |
| desc | string | description what this test is for / all about |
| proto | string | protocols possible option: TCP, UDP, ICMP |
| port | integer | port of the protocol, possible option: TCP: 1-65535 / UDP: 1-65535 / ICMP: 0 |
| expected | integer | possible options: 0: blocked / 1: open / 2: open/filtered / 3: other than above |

## Running the application:

The following is how to execute/run the application as a dockerized container application:

```
shell> make run-docker
```

The output:

![make-run-docker](docs/pics/sample-execution-fw-policy-test.png)

Other execution options:

![make-options](docs/pics/make-options.png)

