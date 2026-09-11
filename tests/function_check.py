#! env python3
from src.nmap_netcheck import *
from src.scapy_netcheck import *

# Run this from the parent path with : sudo python3 -m test.function_check
print("="*50)
print("Test function call checks:")
print("-"*50)

# nmap functions
nmap_icmp = check_icmp("192.168.0.181")
nmap_tcp = check_tcp("192.168.0.181","22")
nmap_udp = check_udp("192.168.0.181","137")
print(f"nmap check ICMP result is : {nmap_icmp}")
print(f"nmap check TCP on port 22 result is : {nmap_tcp}")
print(f"nmap check UDP on port 137 result is : {nmap_udp}")
print("-"*50)

# scapy functions
scapy_icmp = check_icmp_scapy("192.168.0.181")
scapy_tcp = check_tcp_scapy("192.168.0.181",22)
scapy_udp = check_udp_scapy("192.168.0.181",137)
print(f"scapy check ICMP result is : {scapy_icmp}")
print(f"scapy check TCP on port 22 result is : {scapy_tcp}")
print(f"scapy check UDP on port 137 result is : {scapy_udp}")
print("-"*50)
