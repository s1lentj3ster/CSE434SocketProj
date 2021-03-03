import sys
import os
import socket
import string

def receive(host, port):
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.bind(('', port))

    while True:
        message, clientAddress = clientSocket.recvfrom(2048)
        print(message.decode())
        
def send(host, port, mySocket):
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    while True:
        message = raw_input('Say something :3 ')
        print(message)
        mySocket.sendto(message.encode(),(host,port))

        sendMessage, host = mySocket.recvfrom(2048)
        print(sendMessage.decode())
