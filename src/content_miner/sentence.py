"""Contains all the stuff required for building sentences from the Spacy output"""

from typing import Collection

from .spacy_facade import SpaCyToken, SpaCySentence


class Sentence:
    def __init__(self, text: str, targets: Collection[str]):
        self.text = text
        self.targets = targets
        self.target_count = len(targets)
        self.word_count = len(text.split(" "))


def _token_is_interesting(token: SpaCyToken) -> bool:
    return (token.part_of_speech in ['ADJ', 'ADV', 'NOUN', 'VERB']
            and token.lemma.isalpha() and not token.is_stop)


def _get_targets(sentence: SpaCySentence, known_words: Collection[str]) -> Collection[str]:
    return [token.lemma for token in sentence.tokens if _token_is_interesting(token) and token.lemma not in known_words]


def analyse_sentence(spacy_sentence: SpaCySentence, known_words: Collection[str]) -> Sentence:
    """
    Build a sentence object with targets identified and target count stored.
    :param spacy_sentence: sentence to analyse
    :param known_words: list of known words
    :return: analysed sentence
    """
    targets = _get_targets(spacy_sentence, known_words)
    return Sentence(' '.join(spacy_sentence.original_text.split()).strip(), targets)
