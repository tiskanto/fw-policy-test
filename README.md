# fw-policy-test

## Table of Contents
- [What](#what)
- [Why](#why)
- [Use Case](#use-cases)
- [Features](#features)
- [Design Concept](#design-concept)
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

