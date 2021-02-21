#This will handle both join and leave, so we don't have *too* many files :p

import utils
from utils import contactList
from utils import databaseSet
from utils import inProcess

feedback = ''
def join (command):
    if len(command) != 3:
        feedback = 'FAIL.\nPlease enter sufficient parameters.\nUsage: join <contact-list-name> <contact-name>\n'
        return feedback
    listName = command[1]
    contactName = command[2]
    
    #check if name is registered, and list exists, but name does not exist in list yet
    if (contactName in databaseSet) and (listName in contactList)and not(contactName in contactList[listName]):
            
            #ok Im sure there is a more elegant way than this so please feel free to optimize it
            ip = databaseSet[contactName]["IP"]
            port = databaseSet[contactName]["port"]
            #contactList[listName] = {}
            #contactList[listName][contactName] = {}
            #contactList[listName][contactName] = {}
            contactList[listName].update({contactName : { "IP" : ip, "port" : port}})
            #contactList[listName][contactName]['port'] = port
            feedback = 'SUCCESS.\nYou have joined list '+listName+'\n'
    elif (listName in inProcess):
    	feedback = 'FAILURE.\nYou cannot join right now, an IM is in process.\n'
    else:
        feedback = 'FAILURE.\nYou are not registered, or '+listName+' does not exist, or your name is already in '+ listName+'.\n'
    for name, contact in contactList.items():
        print(name , contact , '\n')
    return feedback

def leave (command):
    if len(command) != 3:
        feedback = 'FAIL.\nPlease enter sufficient parameters.\nUsage: leave <contact-list-name> <contact-name>'
        return feedback
    listName = command[1]
    contactName = command[2]
    if (listName in contactList) and (contactName in contactList[listName]) and (contactName in databaseSet):
        contactList[listName].pop(contactName)
        feedback = 'SUCCESS.\nYou have successfully left '+listName+'\n'
    elif (listName in Process):
    	feedback = 'FAILURE.\nYou cannot leave right now, an IM is in process.\n'
    else:
        feedback = 'FAIL.\nYou are not registered, or '+listName+' does not exist, or your name does not exist in this list.\n'
    for name, contact in contactList.items():
        print(name, contact)
    return feedback
