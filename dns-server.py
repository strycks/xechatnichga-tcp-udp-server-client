from dnslib import DNSRecord, DNSHeader, RR, A, QTYPE
from socket import *

# Configuration (CHANGE THIS)
IP_ADDRESS = '127.0.0.1'  # IP Address of TCP/UDP server
DOMAIN = 'abc.com.'       # Domain name to be mapped to TCP/UDP server's ip address              

def dns_response(data):
    request = DNSRecord.parse(data)
    print(f"Request: {request.q.qname}")
    
    reply = DNSRecord(DNSHeader(id=request.header.id, qr=1, aa=1, ra=1), q=request.q)
    
    qname = str(request.q.qname)
    
    if qname == DOMAIN:
        reply.add_answer(RR(qname, QTYPE.A, rdata=A(IP_ADDRESS), ttl=60))
        print(f"Sent {IP_ADDRESS} for {DOMAIN}")
    
    return reply.pack()


dnsServerAddress = '127.0.0.1'  # DNS Server Address
dnsServerPort = 53              # DNS Server Port
udps = socket(AF_INET, SOCK_DGRAM)
udps.bind((dnsServerAddress, dnsServerPort))

print(f"DNS Server started on port {dnsServerPort}...")

while True:
    data, addr = udps.recvfrom(1024)
    response = dns_response(data)
    udps.sendto(response, addr)