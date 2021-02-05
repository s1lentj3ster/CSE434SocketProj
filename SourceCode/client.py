import sys
import os
from socket import *

serverName = sys.argv[1] #<--- Server IP address here 
serverPort = sys.argv[2] #Server's port number
clientSocket = socket (AF_INET, SOCK_DGRAM) #Creates client's socket
message = input('Send me something: ') #Send prompt to client

#Encodes message, attaches destination address and send into clientSocket
clientSocket.sendto(message.encode(), (serverName, serverPort))

#Receives message and address back from server, buffer size 2048
sendMessage, serverAddress = clientSocket.recvfrom(2048)

#Decodes and print receiving message 
print (sendMessage.decode())

#Closes the socket and terminates the process
clientSocket.close()
