import sys
import os
import signal
import multiprocessing
import string
import socket
import time
import pickle
from multiprocessing import *
from collections import OrderedDict
from collections import deque
from socket import *
from string import *

serverName = sys.argv[1] #<--- Server IP address here 
serverPort = int(sys.argv[2]) #Server's port number
clientSocket = socket (AF_INET, SOCK_DGRAM) #Creates client's socket
#port = raw_input('Enter your port: ')
#clientSocket.bind(('',serverPort)) #Use Server port as this provides communication from client to server Port 10000 

#Use Port 10005 for communication Client to Client (Peer to Peer)
chat_Socket = socket(AF_INET, SOCK_DGRAM)
chat_Socket.bind(('',int(10006)))

#clients listening to port 10005 on another thread//Not sure this is needed...?
def client_listening():
  print('Something here to prevent error\n')

def print_list(listName):
    feedback = ''
    feedback += str(len(listName)) +'\n'
    for contactName, detail in listName.items():
        feedback += contactName + '\t'
        for key in detail: 
    		feedback += str(detail[key]) +'\t'
        feedback += '\n'
    print(feedback)
    return
        
def rotate_values(my_dict): #rotate dict values (Is this going to be called in "Send_Message" ? )
    values_deque = deque(my_dict.values())
    keys_deque = deque(my_dict.keys())
    values_deque.rotate(-1)
    keys_deque.rotate(-1)
    return OrderedDict(zip(keys_deque, values_deque))
    
def message_thread():    #Client Listening for incomming messages. 
    while True:
          try:
            test_message, serverAdd = chat_Socket.recvfrom(2048)
            print("Incomming: " + test_message) 
            message = ''

          except OSError:
            break

def send_message(sendto_Host, listIP): #Send message from one client to another?
      while True:
          try:
            print('TODO')            
            clientName = '192.168.10.102' #arbitrary, will need to be filled in by arguement "Sendto_Host" 
            message = "message here " + listIP #dict that was passed from rotate_values definition
            chat_Socket.sendto(message.encode(), (clientName, int(10005))) #Will need to 
          except: 
            break

if (serverPort < 10000 or serverPort > 10499):
    print('Please use port between 10000 and 10499\n')
    exit(1)
message_process = multiprocessing.Process(target = message_thread)
message_process.start()
print('You have been connected to ' + serverName)
while True:
    #sendMessage, serverAddress = clientSocket.recvfrom(2048)
   
  message = raw_input('Enter Command: \n') #Send prompt to client #new line added to prevent issues with input
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
    if ('im-start' not in message):
      print ('test')#sendMessage.decode())
    else: #If the im-start is success, get name and list from command, decodes message to dict
    	if 'FAILURE' not in sendMessage.decode():
    		command = message.split(" ")
    		contact = command[1]
    		name = command[2]
    		contactList = OrderedDict(pickle.loads(sendMessage.decode('base64', 'strict')) ) 
    		#This loop rotates the list until host name is at the top
    		while (list(contactList.keys())[0] != name):
    			contactList = rotate_values(contactList)
    		print_list(contactList)
    		contactList = rotate_values(contactList)
    		nextName = list(contactList)[0]
    		nextIP = contactList[nextName]['IP']
    		nextPort = contactList[nextName]['port']
    		print (nextIP + '\t' + nextPort) #<--- this is next client to send to
    	else: 
    		print(sendMessage.decode()) #<------ Causing duplicate messages on Client
		#only exit with success
  elif 'exit' in message.encode() and 'SUCCESS' in sendMessage.decode():
    clientSocket.close()
    message_process.terminate()
    sys.exit()
    #os._exit(1)
  else:
    sendMessage, serverAddress = clientSocket.recvfrom(2048)
    print (sendMessage.decode())
#Closes the socket and terminates the process
#clientSocket.close()
