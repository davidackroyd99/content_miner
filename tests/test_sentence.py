import unittest
from unittest import mock

from src.content_miner.sentence import _token_is_interesting


class InterestingTokenTestCase(unittest.TestCase):
    def test_is_punct(self):
        token = mock.Mock()
        token.lemma = "."
        token.part_of_speech = "PUNCT"
        token.is_stop = False

        self.assertEqual(_token_is_interesting(token), False)

    def test_is_jibberish(self):
        token = mock.Mock()
        token.lemma = "ajskldf98u32worijfe"
        token.part_of_speech = "ADJ"
        token.is_stop = False

        self.assertEqual(_token_is_interesting(token), False)

    def test_is_stop_word(self):
        token = mock.Mock()
        token.lemma = "tiempo"
        token.part_of_speech = "NOUN"
        token.is_stop = True

        self.assertEqual(_token_is_interesting(token), False)

    def test_is_stop_word(self):
        token = mock.Mock()
        token.lemma = "agua"
        token.part_of_speech = "NOUN"
        token.is_stop = False

        self.assertEqual(_token_is_interesting(token), True)
