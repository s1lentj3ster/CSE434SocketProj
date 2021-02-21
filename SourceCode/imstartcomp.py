#This file will be used for our im start and complete function.
import socket
import utils
from utils import contactList
from utils import databaseSet




def im_start(command):

    feedback = ''
    count = 0
    print("TODO")
    if len(command) != 3:
        feedback = 'FAIL. Please enter in sufficient parameters. Usage: im-start <contact-list-name> <contact-name>\n'
        return feedback
    listName = command[1]
    contactName = command[2]
    if (contactName not in databaseSet):
        feedback = 'FAIL. Contact not registered with server. Please run the register command.\n'
        return feedback
    if (listName not in contactList):
        feedback = 'FAIL. Contact List does not exist. Please create contact list ' + listName+ '\n'
        return feedback
    elif (listName in contactList) and (contactName in databaseSet):
        for contact in contactList[listName]:
            count += 1
        for contacts in contactList:
            feedback += contacts +'\n'
        feedback += str(count) + '\n'
        return feedback
    
    




def im_complete(command):
    print("TODO")

