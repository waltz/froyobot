import unittest
import os

from froyobot.message_validator import isMessageValid 

class TestMessageValidator(unittest.TestCase):

    def test_is_valid_message(self):
        self.assertEqual(isMessageValid("salami hams"), True)

    def test_for_brackets(self):
        """
        Brackets usually mean the message wants a substitution. We don't do
        that, so we should punt the message.
        """

        self.assertEqual(isMessageValid("phong-bread{stuff}"), False)

    def test_minimum_length(self):
        """ Messages should be kinda long-ish. Not just a single word. """

        self.assertEqual(isMessageValid("huh"), False)
