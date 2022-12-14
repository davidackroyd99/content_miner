"""Load files for analysis"""
from typing import Collection
import srt


def _remove_srt(content: str) -> str:
    subs = srt.parse(content)
    return " ".join([s.content for s in subs])


def load_content_file(fp: str) -> str:
    """Get contents of content file as a string"""
    content = ""
    with open(fp, encoding='utf-8') as input_file:
        content = input_file.read()

    if fp[-4:] == ".srt":
        content = _remove_srt(content)

    return content


def load_wordlist_file(fp: str) -> Collection[str]:
    """Get list of known words as a collection of strings"""
    known_words = set()

    with open(fp, encoding='utf-8') as known_file:
        for line in known_file:
            known_words.add(line.strip())

    with open(fp, mode='w', encoding='utf-8') as known_file:
        known_file.write("\n".join(sorted(known_words)))


    return known_words
