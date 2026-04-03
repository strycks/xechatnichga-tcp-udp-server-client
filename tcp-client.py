from socket import *

serverName = 'localhost'
serverPort = 12000
bufSize = 1024
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
mess = str(input('input lowercase sentence: '))
clientSocket.send(mess.encode())
serverMess = clientSocket.recv(bufSize)
print(f'From server: {serverMess.decode()}')
clientSocket.close()
