import scapy.all as s

def scan(ip):
    #s.arping(ip)
    request_arp = s.ARP(pdst=ip)
    #request_arp.pdst=ip
    print(request_arp.summary())
    #s.ls(s.ARP())

scan("192.168.0.1/16")

