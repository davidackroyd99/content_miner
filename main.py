import analysis
import file_loader
from output import print_output

content = file_loader.load_content_file("user/input.txt")
known_words = file_loader.load_wordlist_file("user/known_words.txt")

scan_mode = False
analysed = analysis.analyse_content(content, known_words)

print_output(analysed, scan_mode)
