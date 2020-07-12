from scapy.all import *

send(IP(dst="192.168.220.136")/fuzz(UDP()),loop=1)
