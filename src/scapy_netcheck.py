from scapy.all import *
# has to be run with wheel privilege

test_packet = IP(dst="192.168.0.181")/ICMP()
ret_packet = sr1(test_packet)
ret_packet.show()
ret_packet.command()
hexdump(ret_packet)

