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
    print('Current List\n')
    for c_id, c_info in contactList.items():
        print(c_id)
    print('\n')
    return feedbackMessage

    
    
    

        
         


   # if name in contacts.values():
       # feedbackMessage = 'FAILURE'
       # return contacts, feedbackMessage
    
   # return contacts, feedbackMessage
