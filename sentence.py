"""Contains all the stuff required for building sentences from the Spacy output"""

from typing import Collection


class Sentence:
    def __init__(self, text: str, targets: Collection[str]):
        self.text = text
        self.targets = targets
        self.target_count = len(targets)


def _get_interesting_tokens(sentence) -> Collection[str]:
    return [token for token in sentence if token.pos_ in ['ADJ', 'ADV', 'NOUN', 'VERB']
            and token.lemma_.isalpha() and not token.is_stop]


def analyse_sentence(spacy_sentence, known_words: Collection[str]) -> Sentence:
    """
    Build a sentence object with targets identified and target count stored.
    :param spacy_sentence: sentence to analyse
    :param known_words: list of known words
    :return: analysed sentence
    """
    targets = [token.lemma_ for token in _get_interesting_tokens(spacy_sentence) if token.lemma_ not in known_words]
    return Sentence(' '.join(spacy_sentence.text.split()).strip(), targets)
