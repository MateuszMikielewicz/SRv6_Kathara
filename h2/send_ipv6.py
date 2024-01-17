#!/usr/bin/env python
import sys
import socket
import random
from subprocess import Popen, PIPE
import re

from scapy.all import sendp, get_if_list, get_if_hwaddr
from scapy.all import Ether, IPv6, UDP, TCP


def main():

    if len(sys.argv)<4:
        print('pass 3 arguments: <dst_ip> <dst_mac> "<message>"')
        exit(1)

    addr = sys.argv[1]


    ether_dst = sys.argv[2]
    iface = "eth0"
    
    if not ether_dst:
        print("Mac address for %s was not found in the ARP table" % addr)
        exit(1)

    print("Sending on interface %s to %s" % (iface, str(addr)))
    pkt =  Ether(src=get_if_hwaddr(iface), dst=ether_dst)
    pkt = pkt /IPv6(dst=addr) / sys.argv[3]
    sendp(pkt, iface=iface, verbose=False)

if __name__ == '__main__':
    main()
