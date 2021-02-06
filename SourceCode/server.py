import sys
import os
import string
from socket import *
from string import *
import register
import create
import utils
from utils import databaseSet

#Initialize new Dictionaries for Database



contactList = {}
serverPort = int(sys.argv[1]) 
serverSocket = socket(AF_INET, SOCK_DGRAM)


#Assigns port 10000 to the server's socket
serverSocket.bind(('', serverPort))

#Prints server address and message
print ('IP address: '+ serverSocket.getsockname()[0])
print ('I\'m ready <3 Send me something: ')
messageToClient = 'what did you say?'

#This will be the main database for register
#database = set() <--- Moved to Utils.py file (Global variable)

while True:
    #Receives client message, IP address and port number
    message, clientAddress = serverSocket.recvfrom(2048)
    
    #Processes client's requests and splits into a list of keywords
    command = list(message.decode('latin').split(" "))

    c = command[0]
    if c == "register":
        print("This works too")
       
        
	#Calls register and returns updated database with return message
	databaseSet, messageToClient = register.info(databaseSet, command)
    elif c == "create":

        print('make contact')
        messageToClient = create.createList(command)
        

    elif c == "query-list":
        messageToClient = 'send you contact list'
    elif c == "join":
        messageToClient = 'Join Me bruh'
    elif c == " leave":
        messageToClient = 'Leaving list '
    else: 
        messageToClient = 'IDK what you want, try again, bye'

    #Attach the address to encoded message and send into serverSocket 
    serverSocket.sendto(messageToClient.encode(), clientAddress)
    
''