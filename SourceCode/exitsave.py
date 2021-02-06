import utils
from utils import contactList
from utils import databaseSet

feedback = ''
#contactcount = 0;
#databasecount = 0;
def exit(command):
    if len(command) < 2:
        feedback = 'FAILURE'
        return feedback
    contact_name = command[1]
    if contact_name not in databaseSet:
        feedback = '\nFAILURE. User not registered'
        return feedback
    #Removing from Contact Lists    
    for n in contactList:        
            if contact_name in contactList[n]:
                contactList[n].pop(contact_name)
                #contactcount = contactcount + 1
                print('Removed ' + contact_name + ' from Contact lists')

   
    #Removing from Registered User Database
    if contact_name in databaseSet:
            databaseSet.pop(contact_name)            
            print('Removed ' + contact_name + ' from registered user database')

    feedback = 'SUCCESS'
    print('Removed from lists') #Sanity Check here. Can remove after testing
    return feedback

def save(command):
    count = 0;
    if len(command) < 2:
        feedback = "FAILURE. Please enter file name"
        return feedback
    file_name = command[1]
    save_file = open(file_name, "w")
    
    for contact in databaseSet:
        count += 1
    save_file.write(str(count) + '\n')
    count = 0
    
    for contact in databaseSet:
        save_file.write(contact + ' ' + databaseSet[contact]['IP'] + ' ' + databaseSet[contact]['port'] + '\n')
    save_file.write('\n\n')
    
    for contact in databaseSet:
        count += 1
    save_file.write(str(count) + '\n')
    count = 0
    
    for item in contactList:
        save_file.write(item + "\n")
        for info in contactList[item]:
            save_file.write(info + ' ' + contactList[item][info]['IP'] + ' ' + contactList[item][info]['port'] + '\n')
        save_file.write('\n')
    save_file.close()
    print('Save Success') #Placeholder for now
    feedback = 'SUCCESS'
    return feedback

    
        