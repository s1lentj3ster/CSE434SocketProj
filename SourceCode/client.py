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

# Use Port 10005 for communication Client to Client (Peer to Peer)
chat_Socket = socket(AF_INET, SOCK_DGRAM)


# chat_Socket.bind(('', 10006))


def message_thread():  # Client Listening for incomming messages.
    
    
    while True:
        try:       
            message, serverAdd = chat_Socket.recvfrom(2048)
            message_process(message, serverAdd)
        except OSError:
            break

                
            
def message_process(message, serverAdd):

        listName = ''
        im_message = ''
        nextIP = ''
        nextPort = 0
        sendList = []
        done = True
        while done: 
            try:
                if ('Incoming: ' in message.decode()):
                    im_message = message.decode()
                    print(im_message + ' from ' + serverAdd[0] + ' ' + str(serverAdd[1]))
                    #message = ''
                elif ('List: ' in message.decode()):
                    contact = message.decode()
                    print(contact)
                    listName = contact.replace('List: ', '')
                    #print(listName)
                else:
                    contactList = OrderedDict(pickle.loads(message.decode('base64', 'strict')))
                    utils.print_list(contactList)

                    contactList = utils.rotate_values(contactList)
                    nextName = list(contactList)[0]
                    nextIP = contactList[nextName]['IP']
                    nextPort = contactList[nextName]['port']
                    sendList = pickle.dumps(contactList).encode('base64', 'strict')
		
                    send_message(nextIP, nextPort, sendList, im_message, listName)
                    print ('SUCCESS')
                    done = False
		    
                    message = ''
                break
            except OSError:
                break
    

def send_message(sendto_Host, sendto_Port, listIP, immess, listName):  # Send message from one client to another?
    #while True:
       
            message = immess  # dict that was passed from rotate_values definition
            chat_Socket.sendto(message.encode(), (sendto_Host, int(sendto_Port)))
            # print(sendto_Host + sendto_Port)
            message = 'List: ' + listName
            chat_Socket.sendto(message.encode(), (sendto_Host, int(sendto_Port)))
            message = listIP
            chat_Socket.sendto(message.encode(), (sendto_Host, int(sendto_Port)))
            # print(message)  
            # Will need to
            return
            
      
            
    	
    #return


if (serverPort < 10000 or serverPort > 10499):
    print('Please use port between 10000 and 10499\n')
    exit(1)
message_process = multiprocessing.Process(target=message_thread)
message_process.start()
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
            # These 2 will need to be sent as separate messages, so the list can be decoded properly
            sendList = pickle.dumps(contactList).encode('base64', 'strict')  # <--- Encode list to send over
            im_message = raw_input('Enter Your IM Message: \n')  # <----- GET SENDER MESSAGE HERE
            im_message = 'Incoming: ' + im_message

            send_message(nextIP, nextPort, sendList, im_message, contact)

        else:
            print(sendMessage.decode())
    # only exit with success

# os._exit(1)
# Closes the socket and terminates the process
# clientSocket.close()
