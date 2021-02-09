import socket
import utils
from utils import contactList

def createList(reg): 
    #check for valid perimeter numbers
    if len(reg) != 2 or len(reg[1]) == 0:
        feedbackMessage = 'FAILURE.\nPLease enter sufficient parameters.\n Usage: create <new-list-name>'
        return feedbackMessage
    
    #set name to input
    name = reg[1]

    #check for existing name
    if name in contactList:
        feedbackMessage = 'FAILURE.\nName already exists. Please choose another.\n'
        return feedbackMessage

    contactList[name] = {}
    
    feedbackMessage = 'SUCCESS.\n'+name+' created!\n'
    print('Current List\n')
    for c_id, c_info in contactList.items():
        print(c_id)
    print('\n')
    return feedbackMessage

