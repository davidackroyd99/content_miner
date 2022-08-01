
from collections import Counter

import analysis
import file_loader

content = file_loader.load_content_file("user/input.txt")
known_words = file_loader.load_wordlist_file("user/known_words.txt")

scan_mode = False
analysed = analysis.analyse_content(content, known_words)

print("Percentage of tokens known:", (analysed.token_count - analysed.target_count) / analysed.token_count)
print()

for t, count in Counter(analysed.all_targets).most_common():
    if scan_mode:
        print(t)
        continue
    print(t, count)

    for sent in analysed.sentences:
        if sent.target_count > 0 and sent.targets[0] == t:
            try:
                print(sent.text)
            except:
                print("WARNING: unprintable sentence!")

