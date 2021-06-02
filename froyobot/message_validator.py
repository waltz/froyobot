import re

def isMessageValid(currentMessage):
    """ Determines if a message is valid. """

    return re.search('.*{', currentMessage) == None
