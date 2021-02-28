import sys
import os
import threading
import string
import socket
import time
from threading import *
from socket import *
from string import *

serverName = sys.argv[1] #<--- Server IP address here 
serverPort = int(sys.argv[2]) #Server's port number
clientSocket = socket (AF_INET, SOCK_DGRAM) #Creates client's socket
port = raw_input('Enter your port: ')
clientSocket.bind(('',int(port))) 
chat_Socket = socket(AF_INET, SOCK_DGRAM)
chat_Socket.bind(('',int(10005)))

#clients listening to port 10005 on another thread
def client_listening():    
    while True:
          try:
            test_message, serverAdd = chat_Socket.recvfrom(2048)
            print("Incomming: " + test_message)
            message = ''

          except OSError:
            break

def send_message():
      while True:
          try:
            print('TODO')

def list_contacts(contact_list, iteration):
    print("list TODO\n")


#Recieve list and send message to next person. Will need to extract next name. Set User Variable and if equal, skip, move to next person

if serverPort < 10000 or serverPort > 10499:
    print('Please use port between 10000 and 10499\n')
    exit(1)
thread_message = Thread(target =client_listening)
thread_message.start()
print('You have been connected to ' + serverName)
while True:
    #sendMessage, serverAddress = clientSocket.recvfrom(2048)
   
  message = raw_input('Enter Command: \n') #Send prompt to client
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
        client_listening.daemon = True       
        sys.exit()
  #sendMessage, serverAddress = clientSocket.recvfrom(2048)
  print (sendMessage.decode())
#Closes the socket and terminates the process
#clientSocket.close()
