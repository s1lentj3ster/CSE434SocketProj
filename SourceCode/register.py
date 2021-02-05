import socket

def info (database, reg):
    #This is for success/fail return statements
    feedback = ''	
    try:
        socket.inet_aton(reg[2])
    except:
        feedback = +"Please enter legal IPv4 address.\n Usage: xxx.xxx.xxx.xxx \n"
        return database, feedback

    if 1 >= reg[3] and reg[3] >= 65535:
        feedback += 'Please enter legal port number.\n Usage: 1 <= <port> <= 65535 \n'
        return database, feedback

    database.add((reg[1], reg[2], reg[3]))
    feedback = 'Registration SUCCESS'
    #This function returns the database and feedback string
    return database, feedback
