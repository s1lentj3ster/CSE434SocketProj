#utils.py
from collections import deque
from collections import OrderedDict

global contactList
contactList = {}

    
global databaseSet
databaseSet = {}

global inProcess
inProcess = {}


def rotate_values(my_dict):  # rotate dict values (Is this going to be called in "Send_Message" ? )
    values_deque = deque(my_dict.values())
    keys_deque = deque(my_dict.keys())
    values_deque.rotate(-1)
    keys_deque.rotate(-1)
    return OrderedDict(zip(keys_deque, values_deque))
    
def print_list(listName):
    feedback = ''
    feedback += str(len(listName)) + '\n'
    for contactName, detail in listName.items():
        feedback += contactName + '\t'
        for key in detail:
            feedback += str(detail[key]) + '\t'

        feedback += '\n'
    print(feedback)
    return
