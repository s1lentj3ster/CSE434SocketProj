import sys
import os
import threading
import string
import socket
import peer
from _thread import *
from socket import *
from string import *

serverName = sys.argv[1] #<--- Server IP address here 
serverPort = int(sys.argv[2]) #Server's port number
clientSocket = socket (AF_INET, SOCK_DGRAM) #Creates client's socket
port = raw_input('Enter your port: ')
clientSocket.bind(('',int(port))) 

if serverPort < 10000 or serverPort > 10499:
    print('Please use port between 10000 and 10499\n')
    exit(1)

print('You have been connected to ' + serverName)
while True:
    #sendMessage, serverAddress = clientSocket.recvfrom(2048)
    try:
      sendMessage, serverAddress = clientSocket.recvfrom(2048)
    if 'im-start' not in sendMessage:
      message = raw_input('Enter Command: ') #Send prompt to client
      clientSocket.sendto(message.encode(), (serverName, serverPort))
	  
    #Encodes message, attaches destination address and send into clientSocket
      
    if 'im-start' in message:
         # sendMessage, serverAddress = clientSocket.recvfrom(2048)
      print('Starting IM. Please wait for Server\n')
         

    #Receives message and address back from server, buffer size 2048
    sendMessage, serverAddress = clientSocket.recvfrom(2048)
    if 'initiate-im' in sendMessage.decode():
          print("Host " + 'TODO' + 'initiated instant message with list')
          
    #Decodes and print receiving message 
    print (sendMessage.decode())
		#only exit with success
    if 'exit' in message.encode() and 'SUCCESS' in sendMessage.decode():
        clientSocket.close()
        exit(1)

#Closes the socket and terminates the process
#clientSocket.close()
