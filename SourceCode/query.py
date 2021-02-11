import utils
from utils import contactList

def query_list ():
    #this is return code
    code = 0
    feedback = ''
    
    for name, info in contactList.items():
        feedback += name + '\n' + info
        code +=  1
        for cont in info:
            feedback += info[cont]['IP'] + str(info[cont])
            
            
                 
           

    #this is only temporary, we will have 2 returns, but as of rn the client only reads 1 server message before quitting, but also it works so idk lol
    feedback = str(code)+ '\n'+ feedback.encode(encoding = 'utf-8')
    return feedback
