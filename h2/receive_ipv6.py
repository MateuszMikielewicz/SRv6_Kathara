#!/usr/bin/env python
import sys
import os

from scapy.all import sniff, get_if_list, Ether, get_if_hwaddr, IPv6, Raw

def get_if():
    iface=None
    for i in get_if_list():
        if "eth0" in i:
            iface=i
            break
    if not iface:
        print("Cannot find eth0 interface")
        exit(1)
    return iface

def isNotOutgoing(my_mac):
    def _isNotOutgoing(pkt):
        return pkt[Ether].src != my_mac

    return _isNotOutgoing

def handle_pkt(pkt):
    print("Packet Received:")
    ether = pkt.show()

def main():
    iface = "eth0"
    print("sniffing on %s" % iface)
    sys.stdout.flush()

    my_mac = get_if_hwaddr(get_if())
    my_filter = isNotOutgoing(my_mac)

    sniff(filter="ip6", iface=iface, prn=lambda x: handle_pkt(x), lfilter=my_filter)

if __name__ == '__main__':
    main()

