"""Analyse content and produce an object containing the results"""
from typing import Collection, Set
import unittest

from sentence import Sentence, analyse_sentence
from spacy_facade import get_spacy_document


class AnalysedContent:
    def __init__(self, all_targets: Set[str], sentences: Collection[Sentence], target_count: int, token_count: int):
        self.sentences = sentences
        self.all_targets = all_targets
        self.target_count = target_count
        self.token_count = token_count


def analyse_content(content: str, known_words: Collection[str]):
    """Find all targets within sentences, and count the total number of significant words and targets."""
    doc = get_spacy_document(content)
    scan_set = []
    found_sentences = []
    target_count = 0
    token_count = 0

    for s in doc.sentences:
        sentence = analyse_sentence(s, known_words)
        target_count += len(sentence.targets)
        token_count += sentence.word_count

        for t in sentence.targets:
            scan_set.append(t)
        found_sentences.append(sentence)

    return AnalysedContent(scan_set, found_sentences, target_count, token_count)


class AnalysisIntegrationTestCase(unittest.TestCase):
    def setUp(self) -> None:
        text = "Cuando me despierto, el otro lado de la cama está frío. La cara de Prim es fresca."
        self.analysed_content = analyse_content(text, ["cama", "cuando"])

    def test_token_count(self):
        self.assertEqual(self.analysed_content.token_count, 17)

    def test_target_count(self):
        self.assertEqual(self.analysed_content.target_count, 4)

    def test_all_targets(self):
        self.assertListEqual(self.analysed_content.all_targets, ['despertar', 'frío', 'cara', 'fresca'])




if __name__ == "__main__":
    unittest.main()