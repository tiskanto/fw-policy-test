from scapy.all import *
# has to be run with wheel privilege

# test vars
target_port = 2222
target_addr = "192.168.0.181"

def check_tcp_scapy(tcp_host: str = '127.0.0.1', tcp_port: int = 22) -> int :
    '''
    Function which test TCP connection against a target host
    Returns: integer
    values
    - 0 : tcp port is closed
    - 1 : tcp port is opened
    - 2 : tcp port is silently dropped/timeout
    - 3 : host is unreachable
    - 4 : other than above
    '''
    tcp_pkt = IP(dst=tcp_host)/TCP(dport=tcp_port)
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

check = check_tcp_scapy(target_addr, int(target_port))
print(f"check result: {check}")
