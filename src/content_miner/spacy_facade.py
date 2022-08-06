from typing import Collection

import spacy

nlp = spacy.load("es_core_news_sm")


class SpaCyToken:
    def __init__(self, spacy_token):
        self.lemma: str = spacy_token.lemma_
        self.part_of_speech: str = spacy_token.pos_
        self.is_stop: bool = spacy_token.is_stop


class SpaCySentence:
    def __init__(self, spacy_sentence):
        self.original_text: str = spacy_sentence.text
        self.tokens: Collection[SpaCyToken] = [SpaCyToken(t) for t in spacy_sentence]


class SpaCyDocument:
    def __init__(self, spacy_doc):
        self.sentences: Collection[SpaCySentence] = [SpaCySentence(s) for s in spacy_doc.sents]


def get_spacy_document(text: str) -> SpaCyDocument:
    return SpaCyDocument(nlp(text))
