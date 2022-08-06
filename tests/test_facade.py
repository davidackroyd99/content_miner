import unittest

from src.content_miner.spacy_facade import get_spacy_document, SpaCySentence, SpaCyToken


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
