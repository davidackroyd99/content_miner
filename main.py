import sys

import analysis
import file_loader
from gui import start_gui
from output import print_output

if sys.argv[1] == "gui":
    start_gui()
    exit(0)

content_path = sys.argv[1]
known_words_path = sys.argv[2]
options = sys.argv[3:]
scan_mode = False
freq = True

if "scan" in options:
    scan_mode = True
if "nofreq" in options:
    freq = False

content = file_loader.load_content_file(content_path)
known_words = file_loader.load_wordlist_file(known_words_path)

analysed = analysis.analyse_content(content, known_words)

print_output(analysed, scan_mode, freq)
