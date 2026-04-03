from socket import *

serverPort = 12000
bufSize = 1024
serverName = 'localhost'
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverName, serverPort))
serverSocket.listen(1)
print('Server Initialized')
while True:
    connectionSocket, addr = serverSocket.accept()
    message = connectionSocket.recv(bufSize).decode()
    resMessage = message.upper()
    connectionSocket.send(resMessage.encode())
    connectionSocket.close()
    