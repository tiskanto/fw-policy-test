from scapy.all import *
# has to be run with wheel privilege

# test vars
target_port = 2222
target_addr = "192.168.0.181"

def check_tcp_scapy(tcp_host: str = '127.0.0.1', tcp_port: int = 22) -> int :
    '''
    Function that test TCP connection against a target host
    Returns: integer
    values
    - 0 : tcp port is closed
    - 1 : tcp port is opened
    - 2 : tcp port is silently dropped/timeout
    - 3 : host is unreachable
    - 4 : other than above
    '''
    tcp_payload = "scapy tcp packet test payload"
    tcp_pkt = IP(dst=tcp_host)/TCP(dport=tcp_port)/tcp_payload
    tcp_response = sr1(tcp_pkt, verbose=False, timeout=4)

    if tcp_response is None:
        # packet is being silently dropped due to filter or gets timeout
        return 2
    elif tcp_response.haslayer(ICMP):
        # packt has no routes/unreachable
        return 3
    elif tcp_response.haslayer(TCP):
        # packet return TCP flag syn/ack - open
        if tcp_response[TCP].flags.value == 18 :
            return 1
        # packet return TCP flag rst/ack - closed
        elif tcp_response[TCP].flags.value == 20 :
            return 0
        else:
            # everything else
            return 4
    else:
        # everything else
        return 4

def check_udp_scapy(udp_host: str = '127.0.0.1', udp_port: int = 137) -> int :
    '''
    Function that test UDP connection against a target host
    Returns: integer
    values
    - 0 : udp port is closed
    - 1 : udp port is opened / filtered
    - 2 : network/host unreachable
    - 3 : other than above
    '''
    udp_payload = "scapy udp packet test payload"
    udp_pkt = IP(dst=udp_host)/UDP(dport=udp_port)/udp_payload
    udp_response = sr1(udp_pkt, verbose=False, timeout=4)

    if udp_response is None:
        # packet is being silently dropped or being filtered or open
        return 1
    elif udp_response.haslayer(ICMP):
        # ICMP type destination unreachable
        if udp_response[ICMP].type == 3 :
            # ICMP code port unreachable - closed
            if udp_response[ICMP].code == 3 :
                return 0
            # ICMP code network unreachable
            elif udp_response[ICMP].code == 0 :
                return 2
            # ICMP code host unreachable
            elif udp_response[ICMP].code == 1 :
                return 2
            else:
                # other than above
                return 3
        else:
            # other than above
            return 3
    # making sure we also trap UDP application specific response
    elif udp_response.haslayer(UDP):
        return 1
    else:
        # other than above
        return 3

check_tcp = check_tcp_scapy(target_addr, int(target_port))
check_udp = check_udp_scapy(target_addr, int(target_port))
print(f"TCP check result: {check_tcp}")
print(f"UDP check result: {check_udp}")
