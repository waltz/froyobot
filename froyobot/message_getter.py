import os
import re
import random

from nimrod import Grammar 

class MessageGetter:
    """ This uses Nimrod generate hilarious Yogurt Commercial dialog """

    def __init__(self, dirCandidate = 'resources/data/nimrod'):
        self.basedir = dirCandidate

    def findDataFiles(self):
        files = os.listdir(self.basedir)
        findTextFiles = lambda filename: False if re.search('.*\.txt', filename) is None else True 
        removeExtension = lambda filename: filename[0:-4]
        datafiles = map(removeExtension, filter(findTextFiles, files))

        return list(datafiles)

    def getMessage(self, dataFile):
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

    def shuffle(self):
        dataFiles = self.findDataFiles()

        randomMessage = ''

        while randomMessage == '':
            someDataFile = random.choice(list(dataFiles))
            randomMessage = self.getMessage(someDataFile)

        return randomMessage
