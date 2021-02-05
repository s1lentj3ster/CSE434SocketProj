import sys
import os
import string
from socket import *
from string import *
import register

serverPort = int(sys.argv[1]) 
serverSocket = socket(AF_INET, SOCK_DGRAM)

#Assigns port 10000 to the server's socket
serverSocket.bind(('', serverPort))

#Prints server address and message
print ('IP address: '+ serverSocket.getsockname()[0])
print ('I\'m ready <3 Send me something: ')
messageToClient = 'what did you say?'

#This will be the main database for register
database = set()

while True:
    #Receives client message, IP address and port number
    message, clientAddress = serverSocket.recvfrom(20481)
    
    #Processes client's requests and splits into a list of keywords
    command = list(message.decode().split(" "))

    c = command[0]
    if c == "register":
        print("This works too")
	#Calls register and returns updated database with return message
	database, messageToClient = register.info(database, command)
    elif c == "create":
        print('make contact')
        messageToClient = 'you do  wish to make contact list'
    elif c == "query-list":
        messageToClient = 'send you contact list'
    else: 
        messageToClient = 'IDK what you want, try again, bye'

    #Attach the address to encoded message and send into serverSocket 
    serverSocket.sendto(messageToClient.encode(), clientAddress)
    
''