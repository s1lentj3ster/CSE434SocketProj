import socket
import utils
from utils import databaseSet


def info (reg):
    #This is for success/fail return statements
    feedback = ''

    #Checks paremeter
    if len(reg) != 4:
        feedback += "FAILURE.\nPlease enter sufficient parameters.\nUsage: register <contact-name> <IP-address> <port>\n"
        return feedback
    if len(databaseSet) == 20:
        feedback += 'FAILURE.\nRegister list is full. Please try again later.\n'
        return feedback

    #Checks existing name
    if reg[1] in databaseSet:
        feedback += "FAILURE.\nName already exists\n"
        return feedback

    #Checks valid IPv4 address
    if reg[2].count('.') < 3:
        feedback += "FAILURE.\nPlease enter valid IPv4 address.\nUsage: xxx.xxx.xxx.xxx \n"
        return feedback
    
    #Checks valid port number
    if 10000 >= reg[3] and reg[3] >= 10499:
        feedback += 'FAILURE.\nPlease enter valid port number.\nUsage: 10000 <= <port> <= 10499 \n'
        return feedback
    
    #Adds new person
    databaseSet[reg[1]] = {"IP" : reg[2], "port" : reg[3]}

    feedback = 'SUCCESS.\nYou have been registered. Happy Messaging'
    #This function returns the database and feedback string
    return feedback
