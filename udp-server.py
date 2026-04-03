from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
bufSize = 2048
serverName = 'localhost'
serverSocket.bind((serverName, serverPort))
print('Server Initialized')
while True:
    message, clientAddress = serverSocket.recvfrom(bufSize)
    resMessage = message.decode().upper()
    serverSocket.sendto(resMessage.encode(), clientAddress)