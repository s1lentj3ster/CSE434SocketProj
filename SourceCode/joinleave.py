#This will handle both join and leave, so we don't have *too* many files :p

import utils
from utils import contactList
from utils import databaseSet

feedback = ''
def join (command):
    #if len(command) != 2:
    #    feedback = 'FAIL'
    #    return feedback
    listName = command[1]
    contactName = command[2]
    print(contactList)
    print(databaseSet)
    if (contactName in databaseSet) and (listName in contactList)and not(contactName in contactList[listName]):
            
            #ok Im sure there is a more elegant way than this so please feel free to optimize it
            ip = databaseSet[contactName]["IP"]
            port = databaseSet[contactName]["port"]
            contactList[listName].update({contactName : { "IP" : ip, "port" : port}})
            feedback = 'SUCCESS'
    else:
        feedback = 'FAIL'
    for name, contact in contactList.items():
        print(name , '\t' , contact , '\n')
    return feedback

def leave (command):
    if len(command) != 3:
        feedback = 'FAIL'
        return feedback
    listName = command[1]
    contactName = command[2]
    if (listName in contactList) and (contactName in contactList[listName]):
        contactList[listName].pop(contactName)
        feedback = 'SUCCESS'
    else:
        feedback = 'FAIL'
    for name, contact in contactList.items():
        print(name, contact)
    return feedback
