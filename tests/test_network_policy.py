import pytest
from src.nmap_netcheck import *
from src.scapy_netcheck import *

def test_network_check(case, push_to_pgw):

    # initialise the vars
    check_result = 0
    push_to_pgw.metrics = []

    # Packet test method: nmap
    if case['method'] == 'nmap':
      # ICMP
      if case['proto'] == 'icmp':
          check_result = check_icmp(case['ip'])
          check_expectation = int(case['exp'])
      # TCP
      elif case['proto'] == 'tcp':
          check_result = check_tcp(case['ip'], str(case['port']))
          check_expectation = int(case['exp'])
      # UDP
      elif case['proto'] == 'udp':
          check_result = check_udp(case['ip'], str(case['port']))
          check_expectation = int(case['exp'])
      # Other
      else:
          print("proto input error")
          sys.exit(1)

    # Packet test method: scapy
    # note: in scapy port will be an INT not STR
    if case['method'] == 'scapy':
      # ICMP
      if case['proto'] == 'icmp':
          check_result = check_icmp_scapy(case['ip'])
          check_expectation = int(case['exp'])
      # TCP
      elif case['proto'] == 'tcp':
          check_result = check_tcp_scapy(case['ip'], int(case['port']))
          check_expectation = int(case['exp'])
      # UDP
      elif case['proto'] == 'udp':
          check_result = check_udp_scapy(case['ip'], int(case['port']))
          check_expectation = int(case['exp'])
      # Other
      else:
          print("proto input error")
          sys.exit(1)

    # final results
    final_result = 1.00 if check_result == check_expectation else 0.00

    # assigning attributes to a function
    # ref: https://sethdandridge.com/blog/assigning-attributes-to-python-functions
    push_to_pgw.metrics = [
            {
                "host"  : case['host'].replace(' ', '_'),
                "method": case['method'],
                "ip"    : case['ip'],
                "proto" : case['proto'],
                "port"  : case['port'],
                "exp"   : case['exp'],
                "check_result" : check_result,
                "final_result" : final_result
            }
    ]
    assert check_result == check_expectation

