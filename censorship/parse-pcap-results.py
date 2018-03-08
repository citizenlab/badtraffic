import dpkt
import socket
import collections

PCAP_FILE="test.pcap"
THIS_SRC_IP = "...."


def tcp_flags(flags):
    ret = ''
    if flags & dpkt.tcp.TH_FIN:
        ret = ret + 'F'
    if flags & dpkt.tcp.TH_SYN:
        ret = ret + 'S'
    if flags & dpkt.tcp.TH_RST:
        ret = ret + 'R'
    if flags & dpkt.tcp.TH_ACK:
        ret = ret + 'A'
    if flags & dpkt.tcp.TH_URG:
        ret = ret + 'U'
    if flags & dpkt.tcp.TH_ECE:
        ret = ret + 'E'
    if flags & dpkt.tcp.TH_CWR:
        ret = ret + 'C'
    return ret

pcap = dpkt.pcap.Reader(open(PCAP_FILE, "rb"))
window = collections.deque([], 100)
for ts, buf in pcap:
    eth = dpkt.ethernet.Ethernet(buf)
    if not isinstance(eth.data, dpkt.ip.IP):
        continue
    ip = eth.data
    if not isinstance(ip.data, dpkt.tcp.TCP):
        continue
    tcp = ip.data
    the_data = tcp.data

    if socket.inet_ntoa(ip.src) == THIS_SRC_IP and len(tcp.data) > 0:
        window.append(ip)

    if (ip.id == 13330 and tcp_flags(ip.data.flags) == "RA") in the_data:
        for wip in window:
            if wip.data.sport == tcp.dport:
                print(wip.data.data.split(b"\r\n")[1].split(b":")[1].lstrip().decode("utf-8"))
