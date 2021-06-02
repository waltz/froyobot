import os
import re
import random

from nimrod import Grammar 

from .message_validator import isMessageValid

class MessageGetter:
    """ This uses Nimrod generate hilarious Yogurt Commercial dialog """

    def __init__(self, dirCandidate = 'resources/data/nimrod'):
        self.basedir = dirCandidate

    def findDataFiles(self):
        """ Find a list of test files in the base directory that have message content in them. """

        files = os.listdir(self.basedir)
        findTextFiles = lambda filename: False if re.search('.*\.txt', filename) is None else True 
        removeExtension = lambda filename: filename[0:-4]
        datafiles = map(removeExtension, filter(findTextFiles, files))

        return list(datafiles)

    def getMessage(self, dataFile):
        """
        Take a data file and shove it in to Nimrod. Take the resulting grammar and ask it for a phrase. 
        These grammars have multiple symbols inside of them, sometimes we need to hunt for non-default
        grammars.
        """

        grammar = Grammar()
        grammar.load(self.basedir + '/' + dataFile)

        interpretableSymbols = dict(filter(lambda symbol: symbol[0] != '', grammar.symbols.items()))

        message = ''
        if 'default' in interpretableSymbols:
            message = grammar.interpret('default')
        elif len(interpretableSymbols) > 0:
            firstKey = next(iter(interpretableSymbols))
            message = grammar.interpret(firstKey)

        return message

    def isValidMessage(self, possibleMessage):
        """ Check to see if we really want to hold on to this message. """

        return True

    def shuffle(self):
        """ This method strings it all together, find data files, and extract messages from each file. """

        dataFiles = self.findDataFiles()

        randomMessage = ''

        while randomMessage == '' or isMessageValid(randomMessage) == False:
            someDataFile = random.choice(list(dataFiles))
            randomMessage = self.getMessage(someDataFile)

        return randomMessage
