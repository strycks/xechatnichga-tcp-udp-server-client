from socket import *

serverPort = 25566
bufSize = 1024
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('localhost', serverPort))
serverSocket.listen(1)
print('Server Initialized')
while True:
    connectionSocket, addr = serverSocket.accept()
    message = connectionSocket.recv(bufSize).decode()
    resMessage = message.upper()
    connectionSocket.send(resMessage.encode())
    connectionSocket.close()
    