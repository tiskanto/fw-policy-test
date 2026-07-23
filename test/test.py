#! env python3
from src.nmap_netcheck import *

print("Hello World")
A = check_icmp("192.168.0.181")
B = check_tcp("192.168.0.181","22")
C = check_udp("192.168.0.181","137")
print(f"check ICMP result is : {A}")
print(f"check TCP result is : {B}")
print(f"check UDP result is : {C}")

