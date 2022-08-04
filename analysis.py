"""Analyse content and produce an object containing the results"""
from typing import Collection, Set

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
        token_count += len(sentence.targets)

        for t in sentence.targets:
            scan_set.append(t)
        found_sentences.append(sentence)

    return AnalysedContent(scan_set, found_sentences, target_count, token_count)