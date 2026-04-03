from socket import *

serverPort = 25565
serverSocket = socket(AF_INET, SOCK_DGRAM)
bufSize = 2048
serverSocket.bind(('localhost', serverPort))
print('Server Initialized')
while True:
    message, clientAddress = serverSocket.recvfrom(bufSize)
    resMessage = message.decode().upper()
    serverSocket.sendto(resMessage.encode(), clientAddress)