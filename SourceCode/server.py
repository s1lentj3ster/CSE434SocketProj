import sys
import os
import string
from socket import *
from string import *

serverPort = int(sys.argv[1]) 
serverSocket = socket(AF_INET, SOCK_DGRAM)

#Assigns port 10000 to the server's socket
serverSocket.bind(('', serverPort))

print ('I\'m ready <3 Send me something: ')

while True:
    #Receives client message, IP address and port number
    message, clientAddress = serverSocket.recvfrom(2048)

    #Decodes and turns message to uppercase
    modifiedMessage = message.decode().upper()
    
    #print(message.args[1])
    if message.decode()[0].strip() == 'register':
        print("This works too")
    #Attach the address to encoded message and send into serverSocket 
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)

    #Test Response
    print(modifiedMessage)
