#This file will be used for our im start and complete function.
import socket
import utils
import pickle
from utils import contactList
from utils import databaseSet
from utils import inProcess

def im_start(command):

    feedback = ''
    count = 0
    print("TODO")
    if len(command) != 3:
        feedback = '0\nFAILURE.\nPlease enter in sufficient parameters. Usage: im-start <contact-list-name> <contact-name>\n'
        return feedback
    listName = command[1]
    contactName = command[2]
    if (contactName not in databaseSet):
        feedback = '0\nFAILURE. \nContact not registered with server. Please run the register command.\n'
        return feedback
    if (listName not in contactList):
        feedback = '0\nFAILURE. \nContact List does not exist. Please create contact list ' + listName+ '\n'
        return feedback
    if (contactName not in contactList[listName]):
    	feedback = listName+'\n'+'0\nFAILURE.\nYour name is not in '+listName+'. Please use command \'join <list> <name>\' to join list.\n' 
    	return feedback
    if (inProcess):
    	if(listName in inProcess):
    		feedback = '0\nFAILURE.\nThis list is already in an IM process.\n'
    		return feedback
    if (listName in contactList) and (contactName in databaseSet):
    	inProcess[listName] = contactName
    	print(inProcess)
    	print(contactList[listName])
    	feedback = pickle.dumps(contactList[listName]).encode('base64', 'strict')	
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
        return feedback
    if listName not in inProcess:
    	feedback = 'FAILURE.\nContact List is not engaging in an IM right now.\n'
    	return feedback
    if (contactName not in inProcess[listName]):
    	feedback = 'FAILURE.\nYou did not start this IM Process'
    	return feedback
    else:
    	inProcess.pop(listName)
    	feedback = 'SUCCESS.\nIM completed.\n' 
    return feedback
