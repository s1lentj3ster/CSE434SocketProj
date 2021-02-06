import socket
import utils
from utils import contactList




def createList(reg): 
    name = reg[1]
    for n in contactList:
        if name == contactList[n]:
            feedbackMessage = 'FAILURE'
            return feedbackMessage

    contactList[name] = {}
    
    feedbackMessage = 'SUCCESS'
    print(str(contactList).decode('latin'))
    return feedbackMessage

    
    
    

        
         


   # if name in contacts.values():
       # feedbackMessage = 'FAILURE'
       # return contacts, feedbackMessage
    
   # return contacts, feedbackMessage
