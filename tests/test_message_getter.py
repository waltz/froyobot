import unittest
import os

from froyobot.message_getter import MessageGetter 

class TestMessageGetter(unittest.TestCase):

    def setUp(self):
        self.messageGetter = MessageGetter(os.path.dirname(__file__) + '/fixtures')

    def test_get_data_files(self):
        files = self.messageGetter.findDataFiles()
        files.sort()

        expected = ['blank', 'bird_noises', 'has_a_context', 'dog_noises']
        expected.sort()

        self.assertListEqual(files, expected)

    def test_get_message(self):
        message = self.messageGetter.getMessage('dog_noises')

        self.assertEqual(message, 'bork bork')

    def test_get_non_default_message(self):
        message = self.messageGetter.getMessage('bird_noises')

        self.assertEqual(message, 'cheep cheep')

    def test_no_interpretable_symbols_found(self):
        message = self.messageGetter.getMessage('blank')

        self.assertEqual(message, '')

    def test_contexts_are_ignored(self):
        message = self.messageGetter.getMessage('has_a_context')

        self.assertEqual(message, 'yum')

    def test_shuffle(self):
        message = self.messageGetter.shuffle()

        self.assertIn(message, ['yum', 'bork bork', 'cheep cheep'])
