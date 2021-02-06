import socket
import utils
from utils import databaseSet


def info (reg):
    #This is for success/fail return statements
    feedback = ''

    #Checks paremeter
    if len(reg) != 4:
        feedback += "Register FAIL. Please enter sufficient parameters.\nUsage: register <contact-name> <IP-address> <port>\n"
        return feedback
    
    #Checks existing name
    if reg[1] in databaseSet:
        feedback += "Register FAIL. Name already exists\n"
        return feedback

    #Checks valid IPv4 address
    if reg[2].count('.') < 3:
        feedback += "Register FAIL. Please enter valid IPv4 address.\nUsage: xxx.xxx.xxx.xxx \n"
        return feedback
    
    #Checks valid port number
    if 1 >= reg[3] and reg[3] >= 65535:
        feedback += 'Register FAIL. Please enter valid port number.\nUsage: 1 <= <port> <= 65535 \n'
        return feedback
    
    #Adds new person
    databaseSet[reg[1]] = {"IP" : reg[2], "Port" : reg[3]}

    feedback = 'Registration SUCCESS'
    #This function returns the database and feedback string
    return feedback
