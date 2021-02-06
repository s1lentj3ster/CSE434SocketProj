import socket

def info (database, reg):
    #This is for success/fail return statements
    feedback = ''

    #Checks paremeter
    if len(reg) < 4:
        feedback += "Register FAIL. Please enter sufficient parameters.\nUsage: register <contact-name> <IP-address> <port>\n"
        return database, feedback
    
    #Checks existing name
    for x in database:
        if x[0] == reg[1]:
            feedback += "Register FAIL. Name already exists\n"
            return database, feedback

    #Checks valid IPv4 address
    if reg[2].count('.') < 3:
        feedback += "Register FAIL. Please enter valid IPv4 address.\nUsage: xxx.xxx.xxx.xxx \n"
        return database, feedback
    
    #Checks valid port number
    if 1 >= reg[3] and reg[3] >= 65535:
        feedback += 'Register FAIL. Please enter valid port number.\nUsage: 1 <= <port> <= 65535 \n'
        return database, feedback
    
    #Adds new person
    database.add((reg[1], reg[2], reg[3]))
    feedback = 'Registration SUCCESS'
    #This function returns the database and feedback string
    return database, feedback
