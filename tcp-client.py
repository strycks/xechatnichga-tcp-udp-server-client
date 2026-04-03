from socket import *
import dns.resolver

my_resolver = dns.resolver.Resolver()

my_resolver.nameservers = ['127.0.0.1']
my_resolver.port = 53

answers = my_resolver.resolve('abc.com', 'A')
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
