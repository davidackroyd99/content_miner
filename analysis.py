"""Analyse content and produce an object containing the results"""
from typing import Collection, Set

from sentence import Sentence, analyse_sentence

import spacy

nlp = spacy.load("es_core_news_sm")

class AnalysedContent:
    def __init__(self, all_targets: Set[str], sentences: Collection[Sentence], target_count: int, token_count: int):
        self.sentences = sentences
        self.all_targets = all_targets
        self.target_count = target_count
        self.token_count = token_count


def analyse_content(content: str, known_words: Collection[str]):
    doc = nlp(content)

    scan_set = []
    found_sentences = []
    target_count = 0
    token_count = 0

    for s in doc.sents:
        parsed = analyse_sentence(s, known_words)
        target_count += len(parsed.targets)
        token_count += len(s)

        for t in parsed.targets:
            scan_set.append(t)
        found_sentences.append(parsed)

    return AnalysedContent(scan_set, found_sentences, target_count, token_count)