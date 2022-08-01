import spacy

from collections import Counter

import file_loader
import sentence

nlp = spacy.load("es_core_news_sm")

text = file_loader.load_content_file("user/input.txt")
known_words = file_loader.load_wordlist_file("user/known_words.txt")

doc = nlp(text)

scan_set = []
scan_mode = True
found_sentences = []
target_count = 0
token_count = 0

for s in doc.sents:
    parsed = sentence.analyse_sentence(s, known_words)
    target_count += len(parsed.targets)
    token_count += len(s)

    for t in parsed.targets:
        scan_set.append(t)
    if parsed.target_count == 1 or parsed.target_count == 2:
        found_sentences.append(parsed)

print("Percentage of tokens known:", (token_count - target_count) / token_count)
print()

for t, count in Counter(scan_set).most_common():
    if scan_mode:
        print(t)
        continue
    print(t, count)

    for sent in found_sentences:
        if sent.targets[0] == t:
            try:
                print(sent.text)
            except:
                print("WARNING: unprintable sentence!")

