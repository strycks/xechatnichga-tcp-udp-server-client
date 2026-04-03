from socket import *
import dns.resolver

# Set this to match dns server's address and port.
dnsServerAddress = '127.0.0.1'
dnsServerPort = 53
# Change domain name to match DOMAIN in dns-server.py file
domainName = 'abc.com'

# Resolve domain name
my_resolver = dns.resolver.Resolver()
my_resolver.nameservers = [dnsServerAddress]
my_resolver.port = dnsServerPort
answers = my_resolver.resolve(domainName, 'A')
serverName = str(answers[0])

serverPort = 12000
bufSize = 1024
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
mess = str(input('input lowercase sentence: '))
clientSocket.send(mess.encode())
serverMess = clientSocket.recv(bufSize)
print(f'From server: {serverMess.decode()}')
clientSocket.close()
