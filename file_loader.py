"""Load files for analysis"""
from typing import Collection


def load_content_file(fp: str) -> str:
    """Get contents of content file as a string"""
    with open(fp, encoding='utf-8') as input_file:
        return input_file.read()


def load_wordlist_file(fp: str) -> Collection[str]:
    """Get list of known words as a collection of strings"""
    known_words = []

    with open(fp, encoding='utf-8') as known_file:
        for line in known_file:
            known_words.append(line.strip())

    return known_words
