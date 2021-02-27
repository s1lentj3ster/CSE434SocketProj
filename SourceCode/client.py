import sys
import os
import thread
import string
import socket
import peer
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
         # clientPort = int(10220)
         # client_Host = gethostname()
          #client_IP = gethostbyname(client_Host + '.local')
#
         #im_Message = raw_input('Enter IM: ') #IM Message to send to other devices. 
          #print(client_Host) #Sanity Check
          #print(client_IP) #Sanity Check
          #Need to change PORT and client Socket to other IP's/Ports.
          #Need to have Server send a "Start IM" to the other machines on the list. That could trigger them switching over to 
          #receive from the other client...
          #something to the effect of: if 'im-start': temp-port = serverPort; serverPort = 10300, temp-server = serverName; serverName = next client's IP; 
          #client.Socket.sendto(message.encode(), (serverName,serverPort)
          #send the list and message to the next client and repeat?
          #If perhaps a while loop where if im-compter not in messag, run until im-complete sent/received. Everything swaps back
          #what a pain in the....

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
