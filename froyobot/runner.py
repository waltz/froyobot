import os

from message_getter import MessageGetter

print(MessageGetter(os.path.dirname(__file__) + '/../resources/data/nimrod').shuffle())
