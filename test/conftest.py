import pytest
import yaml
import logging
import os
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway, pushadd_to_gateway

# General configuration
PROM_PGW_ENABLED = int(os.getenv('PROM_PGW_ENABLED',0))
PROM_PGW_HOST = os.getenv('PROM_PGW_HOST','localhost:9091')
TEST_CASE_DIR = os.getcwd() + "/data"
TEST_CASE_FILE_NAME = "test_data.yaml"
TEST_CASE_LOCATION = TEST_CASE_DIR + "/" + TEST_CASE_FILE_NAME

# Logging color codes
yellow = "\x1b[33;20m"
cyan   = "\x1b[36;20m"
reset  = "\x1b[0m"

# Logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format=f'{yellow}[LOG]{reset} %(asctime)s %(levelname)s:{cyan}[%(message)s]{reset}')

def pytest_addoption(parser):

    '''
    Using 'pytest_adoption' hook from pytest to extract
    data from an input file
    '''

    parser.addoption(
            "--case-file",
            action="store",
            default=f"{TEST_CASE_LOCATION}",
            help="Test scenarios data to be executed",
    )

def pytest_generate_tests(metafunc):

    '''
    Using 'pytest_generate_tests' hook to dynamically
    parametrize data from a file. This will get fed
    into test_* file
    '''

    print("\n")
    logging.info(f"PROM_PGW_ENABLED:{PROM_PGW_ENABLED}")
    logging.info(f"PROM_PGW_HOST:{PROM_PGW_HOST}")

    if "case" in metafunc.fixturenames:
        path = metafunc.config.getoption("case_file")
        logging.info(f"TEST_CASE_LOCATION:{path}")

        with open(path,"r") as fd :
            cases = []
            d = yaml.safe_load(fd)
            # re-arranging the YAML data struct into a predefined pytest dict struct
            # format: host, ip, name, proto, port, exp
            for i in d:
                host = i.get('hostname')
                ip = i.get('ip_addr')
                for j in i.get('test_set') :
                    name = j.get('name')
                    proto = j.get('proto')
                    port = j.get('port')
                    exp = j.get('expected')
                    cases.append(
                                   dict(host=host, ip=ip, \
                                   name=name, proto=proto,\
                                   port=port, exp=exp) \
                                )

        ids = [
                f"{c.get('host').replace(' ','_')}-" \
                f"{c.get('ip')}-" \
                f"{c.get('proto')}-" \
                f"{c.get('port')}-" \
                f"expected:{c.get('exp')}" \
                for c in cases
              ]
        metafunc.parametrize("case", cases, ids=ids)

@pytest.fixture(scope='function')
def push_to_pgw():

    '''
    Pushing metrics data to Prometheus Pushgatway
    '''

    push_to_pgw.metrics = []
    yield push_to_pgw

    # push data when prom gateway is enabled
    if PROM_PGW_ENABLED:
        registry = CollectorRegistry()
        for metric in push_to_pgw.metrics :
            metric_name = f"IP-{metric['ip']}-{metric['proto'].upper()}-{metric['port']}"
            g = Gauge(
                        metric_name, \
                        "network_test_result", \
                        labelnames=[
                            'instance',  \
                            'host',      \
                            'ip',        \
                            'proto',     \
                            'port',      \
                            'exp',       \
                            'check_result', \
                            'final_result'  \
                        ], \
                        registry=registry
                     )
            g.labels(
                       'test_instance', \
                        metric['host'], \
                        metric['ip'], \
                        metric['proto'], \
                        metric['port'], \
                        metric['exp'], \
                        metric['check_result'], \
                        metric['final_result'] \
                    ).set(metric['final_result'])
        pushadd_to_gateway(PROM_PGW_HOST, job='perimeter_security_check', registry=registry)

