import re

def isMessageValid(currentMessage):
    """ Determines if a message is valid. """

    if len(currentMessage) < 10:
        return False

    return re.search('.*{', currentMessage) == None
