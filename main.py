import spacy

from collections import Counter

class Sentence():
    def __init__(self, text, targets, target_count):
        self.text = text
        self.targets = targets
        self.target_count = target_count

nlp = spacy.load("es_core_news_sm")

text = ""

with open('user/input.txt', encoding='utf-8') as input_file:
    text = input_file.read()

known_words = []
with open('user/known_words.txt', encoding='utf-8') as known_file:
    for line in known_file:
        known_words.append(line.strip())

doc = nlp(text)

def get_interesting_tokens(sentence):
    return [token for token in sentence if token.pos_ in ['ADJ', 'ADV', 'NOUN', 'VERB'] and token.lemma_.isalpha() and not token.is_stop]

def parse_sentence(sentence):
    targets = [token.lemma_ for token in get_interesting_tokens(sentence) if token.lemma_ not in known_words]
    return Sentence(' '.join(sentence.text.split()).strip(), targets, len(targets))

scan_set = []
scan_mode = True
found_sentences = []
target_count = 0
token_count = 0

for s in doc.sents:
    parsed = parse_sentence(s)
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

