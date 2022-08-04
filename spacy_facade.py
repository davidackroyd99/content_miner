from typing import Collection
import unittest

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


class FacadeSingleSentenceTestCase(unittest.TestCase):
    def setUp(self) -> None:
        test_text = "Ella es guapa."
        self.doc = get_spacy_document(test_text)

    def test_doc(self):
        self.assertEqual(len(self.doc.sentences), 1)

    def test_sentence(self):
        s: SpaCySentence = self.doc.sentences[0]

        self.assertEqual(len(s.tokens), 4)
        self.assertEqual(s.original_text, "Ella es guapa.")

    def test_tokens(self):
        t2: SpaCyToken = self.doc.sentences[0].tokens[2]

        self.assertEqual(t2.lemma, "guapo")
        self.assertEqual(t2.part_of_speech, "ADJ")

        t3: SpaCyToken = self.doc.sentences[0].tokens[3]

        self.assertEqual(t3.lemma, ".")
        self.assertEqual(t3.part_of_speech, "PUNCT")


if __name__ == "__main__":
    unittest.main()

    # assert(doc.sentences[0].original_text == test_text)
    # assert(doc.sentences[0].tokens[0].part_of_speech == "PRON")