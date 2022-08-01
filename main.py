import spacy

from collections import Counter

import sentence

nlp = spacy.load("es_core_news_sm")

text = ""

with open('user/input.txt', encoding='utf-8') as input_file:
    text = input_file.read()

known_words = []
with open('user/known_words.txt', encoding='utf-8') as known_file:
    for line in known_file:
        known_words.append(line.strip())

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

