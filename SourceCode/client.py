import sys
import os
import string
import socket
from socket import *
from string import *

serverName = sys.argv[1] #<--- Server IP address here 
serverPort = int(sys.argv[2]) #Server's port number
clientSocket = socket (AF_INET, SOCK_DGRAM) #Creates client's socket

if serverPort < 10000 or serverPort > 10499:
    print('Please use port between 10000 and 10499\n')
    exit(1)

print('You have been connected to ' + serverName)
while True:
    message = raw_input('Enter Command: ') #Send prompt to client

    #Encodes message, attaches destination address and send into clientSocket
    clientSocket.sendto(message.encode(), (serverName, serverPort))

    #Receives message and address back from server, buffer size 2048
    sendMessage, serverAddress = clientSocket.recvfrom(2048)

    #Decodes and print receiving message 
    print (sendMessage.decode())
    if 'exit' in message.encode():
        clientSocket.close()
        exit(1)

#Closes the socket and terminates the process
#clientSocket.close()
