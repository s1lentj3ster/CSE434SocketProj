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

# Use Dynamic Port get for communication Client to Client (Peer to Peer)
chat_Socket = socket(AF_INET, SOCK_DGRAM)

def message_thread():  # Client Listening for incomming messages.
    while True:
        try:       
            message, serverAdd = chat_Socket.recvfrom(2048)
            nextIP, nextPort, sendList, im_message, listName, count = message_processing(message, serverAdd)
            if (count > 0):
            	send_message(nextIP, nextPort, sendList, im_message, listName, count)
            else:
            	print('SUCCESS\n')
        except OSError:
            break
    return    
def message_processing(message, serverAdd): #Processes and prints incoming peer message
        listName = ''
        nextIP = ''
        nextPort = 0
        sendList = []

        try: #Decodes message list
            output = list(pickle.loads(message.decode('base64','strict')))
            im_message = output[1] # Peer Message
	    listName = output[0]   # List Name       
            contactList = output[2] # IP List 
            count = int(output[3]) - 1 # Message TTL, decreases for every send
            print('Incoming: ' + im_message + ' from ' + serverAdd[0] + ' ' + str(serverAdd[1]))
	    print ('List: ' + listName)
	    # Decodes the list
            contactList = OrderedDict(pickle.loads(contactList.decode('base64', 'strict')))
            utils.print_list(contactList)
	    # Rotates list to next peer, gets IP, Port 
            contactList = utils.rotate_values(contactList)
            nextName = list(contactList)[0]
            nextIP = contactList[nextName]['IP']
            nextPort = contactList[nextName]['port']
            #Encodes list
            sendList = pickle.dumps(contactList).encode('base64', 'strict')
	    return nextIP, nextPort, sendList, im_message, listName, count 
        except OSError:
    	    return

def send_message(sendto_Host, sendto_Port, listIP, immess, listName, count):  # Send message from one client to another?
       	    send = [immess, listName, listIP, count] #Wraps everything in one list
       	    send = pickle.dumps(send).encode('base64', 'strict') #encode list
       	    chat_Socket.sendto(send.encode(), (sendto_Host, int(sendto_Port))) #Send to next peer
            return

if (serverPort < 10000 or serverPort > 10499):
    print('Please use port between 10000 and 10499\n')
    exit(1)

#Initiates the chat socket listener     
message_process = multiprocessing.Process(target=message_thread)
message_process.start()

#Client-Server interaction
print('You have been connected to ' + serverName)
while True:
    message = raw_input('Enter Command: \n')  # Send prompt to client #new line added to prevent issues with input
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    # splits commands into args
    command = message.split(" ")
    # Receives message and address back from server, buffer size 2048
    sendMessage, serverAddress = clientSocket.recvfrom(2048)

    if ('im-start' not in message):
        print(sendMessage.decode())
        # exit system
        if 'exit' in message and 'SUCCESS' in sendMessage.decode():
            clientSocket.close()
            message_process.terminate()
            sys.exit()
        elif 'register' in message and 'SUCCESS' in sendMessage.decode():
            hostPort = command[3]  # <----- we can bind host to this value
            chat_Socket.bind((str(command[2]), int(hostPort)))
            #chat_Socket.setsockopt(IPPROTO_IP,IP_MULTICAST_TTL,20)
            print('Started Message_Process')


    else:  # If the im-start is success, get name and list from command, decodes message to dict
        if 'FAILURE' not in sendMessage.decode():
            print('Starting IM. Please wait for Server\n')
            contact = command[1]  # get contact list name
            name = command[2]  # get name
            contactList = OrderedDict(pickle.loads(sendMessage.decode('base64', 'strict')))
            # This loop rotates the list until host name is at the top
            while (list(contactList.keys())[0] != name):
                contactList = utils.rotate_values(contactList)
            utils.print_list(contactList)
	    
            # Rotate next peer on top
            contactList = utils.rotate_values(contactList)
            nextName = list(contactList)[0]
            nextIP = contactList[nextName]['IP']
            nextPort = contactList[nextName]['port']
            # print(nextPort)
            sendList = pickle.dumps(contactList).encode('base64', 'strict')  # <--- Encode list to send over
            im_message = raw_input('Enter Your IM Message: \n')  # <----- GET SENDER MESSAGE HERE
            
            count = str(len(contactList))
            #Calls sender function
            send_message(nextIP, nextPort, sendList, im_message, contact, count)

        else:
            print(sendMessage.decode())
    # only exit with success

# os._exit(1)
# Closes the socket and terminates the process
# clientSocket.close()
