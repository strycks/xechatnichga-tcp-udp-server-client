from socket import *
serverName = '10.11.67.47'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
message = input('Input lowercase sentence: ')
clientSocket.send(message.encode())
modifiedMessage = clientSocket.recv(2048)
print('From Server:', modifiedMessage.decode())
clientSocket.close()