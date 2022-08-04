"""Contains all the stuff required for building sentences from the Spacy output"""

from typing import Collection
import unittest
from unittest import mock

from spacy_facade import SpaCyToken, SpaCySentence


class Sentence:
    def __init__(self, text: str, targets: Collection[str]):
        self.text = text
        self.targets = targets
        self.target_count = len(targets)


def _token_is_interesting(token: SpaCyToken) -> bool:
    return (token.part_of_speech in ['ADJ', 'ADV', 'NOUN', 'VERB']
            and token.lemma.isalpha() and not token.is_stop)


def _get_targets(sentence: SpaCySentence, known_words: Collection[str]) -> Collection[SpaCyToken]:
    return [token for token in sentence.tokens if _token_is_interesting(token) and token.lemma in known_words]


def analyse_sentence(spacy_sentence: SpaCySentence, known_words: Collection[str]) -> Sentence:
    """
    Build a sentence object with targets identified and target count stored.
    :param spacy_sentence: sentence to analyse
    :param known_words: list of known words
    :return: analysed sentence
    """
    targets = _get_targets(spacy_sentence, known_words)
    return Sentence(' '.join(spacy_sentence.text.split()).strip(), targets)


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


# class AnalyseSentenceTestCase(unittest.TestCase):



if __name__ == "__main__":
    unittest.main()
