#!/usr/bin/python3

"""
Attack towards the `tcp-phone-plug` policy of the TP-Link smart plug.
Issue commands to the smart plug, which has not issued an ARP request beforehand,
by sending TCP packets with the following signature:
    - Source MAC address:       3c:cd:5d:a2:a9:d7 (phone MAC address)
    - Destination MAC address:  50:c7:bf:ed:0a:54 (TP-Link smart plug MAC address)
    - Source IPv4 address:      192.168.1.223 (phone IPv4 address)
    - Destination IPv4 address: 192.168.1.135 (TP-Link smart plug IPv4 address)
    - Destination TCP port:     9999
All packets should be blocked.
"""

import scapy.all as scapy
import random

### GLOBAL VARIABLES ###
mac_src  = "3c:cd:5d:a2:a9:d7"
mac_dst  = "50:c7:bf:ed:0a:54"
ip_src   = "192.168.1.223"
ip_dst   = "192.168.1.135"
port_dst = 9999


### FUNCTIONS ###
def main():
    port_src = random.randint(1024, 65535)
    packet = scapy.Ether(src=mac_src, dst=mac_dst) / scapy.IP(src=ip_src, dst=ip_dst) / scapy.TCP(sport=port_src, dport=port_dst)
    packet = packet.__class__(bytes(packet))
    scapy.sendp(packet, iface="enp0s31f6", count=5, verbose=False)


### MAIN PROGRAM ###
if __name__ == "__main__":
    main()
