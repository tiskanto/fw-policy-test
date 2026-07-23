import nmap

# icmp test scan
def check_icmp(icmp_host: str = '127.0.0.1') -> int :
    '''
    Function which test ICMP echo against a target host
    Returns: integer
    values
    - 1 : pingable via ICMP ECHO
    - 0 : NOT pingable via ICMP ECHO
    '''
    nm_icmp = nmap.PortScanner()
    nm_icmp.scan(hosts=icmp_host, arguments='-sn -PE', timeout=3, sudo=True)
    if int(nm_icmp._scan_result['nmap']['scanstats']['downhosts']) :
        return 0
    else:
        return 1

# udp test scan
def check_udp(udp_host: str = '127.0.0.1', udp_port: str = '137') -> int :
    '''
    Function which test UDP port against a target host
    Returns: integer
    values
    - 0 : closed
    - 1 : open
    - 2 : open | filtered
    - 3 : other than above
    '''
    nm_udp = nmap.PortScanner()
    nm_udp.scan(hosts=udp_host, ports=udp_port, arguments='-sU', timeout=3, sudo=True)
    udp_state = nm_udp._scan_result['scan'][udp_host]['udp'][int(udp_port)]['state']
    if udp_state == 'open' :
        return 1
    elif udp_state == 'closed' :
        return 0
    elif udp_state == 'open|filtered' :
        return 2
    else:
        return 3

# tcp test scan
def check_tcp(tcp_host: str = '127.0.0.1', tcp_port: str = '22') -> int :
    '''
    Function which test TCP port against a target host
    Returns: integer
    values
    - 0 : closed
    - 1 : open
    - 2 : filtered
    - 3 : other than above
    '''
    nm_tcp = nmap.PortScanner()
    nm_tcp.scan(hosts=tcp_host, ports=tcp_port, arguments='-sT', timeout=3, sudo=True)
    tcp_state = nm_tcp._scan_result['scan'][tcp_host]['tcp'][int(tcp_port)]['state']
    if tcp_state == 'open' :
        return 1
    elif tcp_state == 'closed' :
        return 0
    elif tcp_state == 'filtered' :
        return 2
    else:
        return 3

