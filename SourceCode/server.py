import sys
import os
import string
import threading
import socket
import subprocess
import time
from socket import *
from string import *
import threading
from threading import *
import register
import create
import utils
import query
import joinleave
import exitsave
import imstartcomp
from utils import databaseSet
from utils import contactList


#Initialize new Dictionaries for Database


serverPort = int(sys.argv[1]) 
serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket_2 = socket(AF_INET, SOCK_DGRAM)
serverSocket_2.bind(('',10005))#4Client Send port?
#Assigns port to the server's socket
if serverPort < 10000 or serverPort > 10499:
    print("Please enter in a port number between 10000 to 10499\n")
    exit(1)
serverSocket.bind(('', serverPort))



def multithread_server(client_stuff, clients_message):
    message_test = str(clients_message)
    listen_system_ip = str(client_stuff)
    listen_system_port = 10005
    listen_system = (listen_system_ip, listen_system_port)
    serverSocket_2.sendto(message_test, listen_system)
    return
    


Server_Name = gethostname()
Server_IP = gethostbyname(Server_Name + '.local')

#Prints server address and message
print ('Connecting...\n')
print('Server Name: ' + Server_Name)
print('Servers IP address: ' + Server_IP)
print('Server monitoring port ' + str(serverPort))

messageToClient = ''
block_comms = False

while True:
    print ('Awaiting instruction from a client...')
    
    
    #Receives client message, IP address and port number
    message, clientAddress = serverSocket.recvfrom(2048)
    
    
    #Processes client's requests and splits into a list of keywords
    command = list(message.decode('latin').split(" "))
    
   
   
    c = command[0]
    print(c.capitalize() + " process requested by client at IP " + str(clientAddress[0]))
    if "register" in c.lower():
        if len(command) > 3:        
            print("Registering " + command[1])
        #Calls register and returns updated database with return message
            messageToClient = register.info(command)
        
        else:
            print('Error: Registration Failed by Client at IP ' + str(clientAddress[0]))
            messageToClient = 'Register FAIL. Please enter sufficient parameters. \nUsage: register <contact-name> <IP-address> <port>\n'    
        
    elif "create" in c.lower():
        messageToClient = create.createList(command)
        

    elif "query-list" in c.lower():        
        messageToClient = query.query_list()

    elif "join" in c.lower():
        if block_comms != True:        
            print("Joining " + command[1])
            messageToClient = joinleave.join(command)
        else:
            messageToClient = 'Cannot join ' + command[1] + ' while IM in Progress\n'        

    elif "leave" in c.lower():
        if block_comms != True: 
            print("Registered User " + command[2] + ' requesting to leave ' + command[1] + ' list..')
            messageToClient = joinleave.leave(command)        
        else:
            messageToClient = 'Cannot leave ' + command[1] + ' while IM in Progress\n' 
    elif "exit" in c.lower():
        if block_comms != True:         
            messageToClient = exitsave.exit(command)
        else:
            messageToClient = 'Cannot exit while IM in progress\n' 
    elif 'save' in c.lower():
        messageToClient = exitsave.save(command)

    elif 'im-start' in c.lower():
        messageToClient = imstartcomp.im_start(command)
        block_comms = True
        messageToClient += 'initiate-im\n' #honestly don't know if this will work...
        im_message = 'Oh ok, its messaging time\n'
        t1 = threading.Thread(target=multithread_server('192.168.10.102', im_message))
        t1.start()
    
    elif 'im-complete' in c.lower():
    	messageToClient = imstartcomp.im_complete(command)
        print("Done\n")
        block_comms = False
    else: 
        messageToClient = 'INVALID COMMAND. Please try again'
        print('ALERT! Invalid command ' + '"' + c.capitalize() + '" entered by Client at IP ' + str(clientAddress[0]))

    #Attach the address to encoded message and send into serverSocket 
    serverSocket.sendto(messageToClient.encode(), clientAddress)
    messageToClient = ''
    
    

