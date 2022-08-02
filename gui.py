import tkinter as tk

import analysis
import cache
import file_loader
from output import save_output


def start_gui():
    window = tk.Tk()

    greeting = tk.Label(text="Content Miner v0.1")
    greeting.pack()

    content_frame = tk.Frame()
    content_label = tk.Label(master=content_frame, text="Content path:")
    content_label.grid(row=0, column=0)
    content_entry = tk.Entry(master=content_frame, width=80)
    content_entry.insert(0, cache.read_key(cache.CacheKey.CONTENT_PATH))
    content_entry.grid(row=0, column=1)

    content_frame.pack()

    known_words_frame = tk.Frame()
    known_words_label = tk.Label(master=known_words_frame, text="Known word list path:")
    known_words_label.grid(row=0, column=0)
    known_words_entry = tk.Entry(master=known_words_frame, width=80)
    known_words_entry.insert(0, cache.read_key(cache.CacheKey.KNOWN_WORDS_PATH))
    known_words_entry.grid(row=0, column=1)

    known_words_frame.pack()

    destination_frame = tk.Frame()
    destination_label = tk.Label(master=destination_frame, text="Destination path:")
    destination_label.grid(row=0, column=0)
    destination_entry = tk.Entry(master=destination_frame, width=80)
    destination_entry.insert(0, cache.read_key(cache.CacheKey.DESTINATION_PATH))
    destination_entry.grid(row=0, column=1)

    destination_frame.pack()

    options_frame = tk.Frame()
    targets_only = tk.IntVar(value=0)
    targets_only_tickbox = tk.Checkbutton(master=options_frame, text="Targets Only", variable=targets_only)
    targets_only_tickbox.grid(row=0, column=0)

    show_freq = tk.IntVar(value=1)
    show_freq_tickbox = tk.Checkbutton(master=options_frame, text="Show Target Frequency", variable=show_freq)
    show_freq_tickbox.grid(row=0, column=1)

    target_count_label = tk.Label(master=options_frame, text="Max targets:")
    target_count_label.grid(row=0, column=2)
    target_count = tk.Entry(master=options_frame, width=2)
    target_count.insert(0, "1")
    target_count.grid(row=0, column=3)

    options_frame.pack()

    def update_cache():
        cache.update_key(cache.CacheKey.CONTENT_PATH, content_entry.get())
        cache.update_key(cache.CacheKey.KNOWN_WORDS_PATH, known_words_entry.get())
        cache.update_key(cache.CacheKey.DESTINATION_PATH, destination_entry.get())

    def find_sentences():
        update_cache()

        content = file_loader.load_content_file(content_entry.get())
        known_words = file_loader.load_wordlist_file(known_words_entry.get())

        analysed = analysis.analyse_content(content, known_words)
        save_output(analysed, destination_entry.get(), bool(targets_only.get()), bool(show_freq.get()), int(target_count.get()))

    button = tk.Button(text="Find sentences", command=find_sentences)
    button.pack()
    
    window.mainloop()