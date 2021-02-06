def create(contacts, name):
    feedbackMessage = ''
    if name in contacts.values():
        feedbackMessage = 'FAILURE'
        return contacts, feedbackMessage
    
    return contacts, feedbackMessage
