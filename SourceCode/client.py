import sys
import os
import signal
import multiprocessing
import string
import socket
import time
import pickle
import utils
from multiprocessing import *
from collections import OrderedDict
from socket import *
from string import *

serverName = sys.argv[1]  # <--- Server IP address here 
serverPort = int(sys.argv[2])  # Server's port number
clientSocket = socket(AF_INET, SOCK_DGRAM)  # Creates client's socket
# port = raw_input('Enter your port: ')
# clientSocket.bind(('',serverPort)) #Use Server port as this provides communication from client to server Port 10000 

# Use Port 10005 for communication Client to Client (Peer to Peer)
chat_Socket = socket(AF_INET, SOCK_DGRAM)
chat_Socket.bind(('', 10006))

def message_thread():  # Client Listening for incomming messages. 
    while True:
        try:
            #print('Working at this point')
            test_message, serverAdd = chat_Socket.recvfrom(2048)
            print("Incomming: " + test_message.decode() + str(serverAdd))
            message = ''

        except OSError:
            break

def send_message(sendto_Host, listIP, immess):  # Send message from one client to another?
    while True:
        try:
            #print('TODO')
             # arbitrary, will need to be filled in by arguement "Sendto_Host" 
            message = immess  # dict that was passed from rotate_values definition
            print(message)
            chat_Socket.sendto(message.encode(), (sendto_Host, 10006))  # Will need to
            break
        except OSError:
            break


# Error checking IP enter. Otherwise,
client_Hostname = gethostname()
client_IP = gethostbyname(client_Hostname + '.local')

if (serverPort < 10000 or serverPort > 10499):
    print('Please use port between 10000 and 10499\n')
    exit(1)
message_process = multiprocessing.Process(target=message_thread)
message_process.start()
print('You have been connected to ' + serverName)
while True:
    message = raw_input('Enter Command: \n')  # Send prompt to client #new line added to prevent issues with input
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    #splits commands into args
    command = message.split(" ")
    # Receives message and address back from server, buffer size 2048
    sendMessage, serverAddress = clientSocket.recvfrom(2048)

    if ('im-start' not in message):
	print(sendMessage.decode())
    	#exit system
    	if 'exit' in message and 'SUCCESS' in sendMessage.decode():
        	clientSocket.close()
        	message_process.terminate()
        	sys.exit()
        elif 'register' in message and 'SUCCESS' in sendMessage.decode(): 
        	hostPort = command[3] #<----- we can bind host to this value
        	
    else:  # If the im-start is success, get name and list from command, decodes message to dict
        if 'FAILURE' not in sendMessage.decode():
            print('Starting IM. Please wait for Server\n')
            contact = command[1] #get contact list name
            name = command[2] #get name
            contactList = OrderedDict(pickle.loads(sendMessage.decode('base64', 'strict')))
            # This loop rotates the list until host name is at the top
            while (list(contactList.keys())[0] != name):
                contactList = utils.rotate_values(contactList)
            utils.print_list(contactList)
            
            #Rotate next peer on top
            contactList = utils.rotate_values(contactList) 
            nextName = list(contactList)[0]
            nextIP = contactList[nextName]['IP']
            nextPort = contactList[nextName]['port']
            
            #These 2 will need to be sent as separate messages, so the list can be decoded properly
            sendList = pickle.dumps(contactList).encode('base64', 'strict') #<--- Encode list to send over
            im_message = raw_input('Enter Your IM Message: \n') #<----- GET SENDER MESSAGE HERE
            
            send_message(nextIP, sendList, im_message)
            #sendingMessage = multiprocessing.Process(target=send_message(nextIP,contactList,im_message)) #<--- additional process unneeded. 
            #sendingMessage.start()
            #print(nextIP + '\t' + nextPort)  # <--- this is next client to send to
        else:
            print(sendMessage.decode())  
    # only exit with success
    
# os._exit(1)
# Closes the socket and terminates the process
# clientSocket.close()
