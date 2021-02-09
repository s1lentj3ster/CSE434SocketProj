import sys
import os
import string
import socket
from socket import *
from string import *
import register
import create
import utils
import query
import joinleave
import exitsave
from utils import databaseSet
from utils import contactList

#Initialize new Dictionaries for Database

#contactList = {}
serverPort = int(sys.argv[1]) 
serverSocket = socket(AF_INET, SOCK_DGRAM)


#Assigns port to the server's socket
if serverPort < 10000 or serverPort > 10499:
    print("Please enter in a port number between 10000 to 10499\n")
    exit(1)
serverSocket.bind(('', serverPort))


Server_Name = gethostname()
Server_IP = gethostbyname(Server_Name + '.local')

#Prints server address and message
print ('Connecting...\n')
print('Servers IP address: ' + Server_IP)
print('Server monitoring port ' + str(serverPort))

messageToClient = ''


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
            print('ERROR')
            messageToClient = 'Register FAIL. Please enter sufficient parameters. \nUsage: register <contact-name> <IP-address> <port>\n'    
        
    elif c == "create":       
        messageToClient = create.createList(command)

    elif c == "query-list":	
        messageToClient = query.query_list()
       
    elif c == "join":
        messageToClient = joinleave.join(command)

    elif c == "leave":
        messageToClient = joinleave.leave(command)

    elif c == "exit":
        messageToClient = exitsave.exit(command)
    elif c == 'save':
        messageToClient = exitsave.save(command)
              
    else: 
        messageToClient = 'INVALID COMMAND. Please try again'
        print('ALERT! Invalid command ' + '"' + c.capitalize() + '" entered by Client at IP ' + str(clientAddress[0]))

    #Attach the address to encoded message and send into serverSocket 
    serverSocket.sendto(messageToClient.encode(), clientAddress)
    

