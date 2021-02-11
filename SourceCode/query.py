import utils
from utils import contactList

def query_list ():
    #this is return code
    code = 0
    feedback = ''
    
    for name, info in contactList.items():
        feedback += name  + '\n' + str(contactList.get(name)) + '\n'
        code +=  1
        
            
            
                 
           

    #this is only temporary, we will have 2 returns, but as of rn the client only reads 1 server message before quitting, but also it works so idk lol
    feedback = str(code)+ '\n'+ feedback.encode(encoding = 'utf-8')
    return feedback
