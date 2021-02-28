#This file will be used for our im start and complete function.
import socket
import utils
from utils import contactList
from utils import databaseSet
from utils import inProcess

def im_start(command):

    feedback = ''
    count = 0
    print("TODO")
    if len(command) != 3:
        feedback = 'FAILURE.\nPlease enter in sufficient parameters. Usage: im-start <contact-list-name> <contact-name>\n'
        return feedback
    listName = command[1]
    contactName = command[2]
    if (contactName not in databaseSet):
        feedback = 'FAILURE.\n Contact not registered with server. Please run the register command.\n'
        return feedback
    if (listName not in contactList):
        feedback = 'FAILURE.\n Contact List does not exist. Please create contact list ' + listName+ '\n'
        return feedback
    elif (listName in contactList) and (contactName in databaseSet):
    	#inProcess = {contactList : listName}
        feedback += listName + '\n'
        feedback += str(len(contactList[listName])) +'\n'
        for contactName, detail in contactList[listName].items():
            feedback += contactName + '\t'
            for key in detail: 
        	feedback += str(detail[key]) +'\t'
            feedback += contactList + '\n'	
        return feedback

def im_complete(command):
    print("TODO")
    feedback = ''
    if len(command) != 3:
        feedback = 'FAILURE.\nPlease enter in sufficient parameters. Usage: im-start <contact-list-name> <contact-name>\n'
        return feedback
    listName = command[1]
    contactName = command[2]
    if (contactName not in databaseSet):
        feedback = 'FAILURE.\nContact not registered with server. Please run the register command.\n'
        return feedback
    if (listName not in contactList):
        feedback = 'FAILURE.\nContact List does not exist. Please create contact list ' + listName+ '\n'
    if listName not in inProcess:
    	feedback = 'FAILURE.\nContact List is not engaging in an IM right now.\n'
    else:
    	inProcess.pop(contactList, listName)
    	feedback = 'SUCCESS.\nIM completed.\n' 
    return feedback
