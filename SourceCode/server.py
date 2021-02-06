import sys
import os
import string
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

#Prints server address and message
print ('IP address: '+ serverSocket.getsockname()[0])
print ('I\'m ready <3 Send me something: ')
messageToClient = ''


while True:
    #Receives client message, IP address and port number
    message, clientAddress = serverSocket.recvfrom(2048)
    
    #Processes client's requests and splits into a list of keywords
    command = list(message.decode('latin').split(" "))

    c = command[0]
    if c == "register":
        print("Registering " + command[1])
        #Calls register and returns updated database with return message
        messageToClient = register.info(command)
        
    elif c == "create":
        print('make contact')
        messageToClient = create.createList(command)

    elif c == "query-list":
	#returnQuery = ''
        messageToClient = query.query_list()
        #serverSocket.sendto(returnQuery, clientAddress)

    elif c == "join":
        messageToClient = 'Join Me bruh '+joinleave.join(command)

    elif c == "leave":
        messageToClient = 'Leaving list '+joinleave.leave(command)

    elif c == "exit":
        messageToClient = 'Exiting Everything' + exitsave.exit(command)
    elif c == 'save':
        messageToClient = 'Saving File ' + exitsave.save(command)
              
    else: 
        messageToClient = 'IDK what you want, try again, bye'

    #Attach the address to encoded message and send into serverSocket 
    serverSocket.sendto(messageToClient.encode(), clientAddress)
    

