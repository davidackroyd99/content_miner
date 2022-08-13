import tkinter as tk
from tkinter import messagebox

from .analysis import analyse_content
from .cache import *
from .file_loader import *
from .output import save_output
from .profiler import profiler


def start_gui():
    window = tk.Tk()

    greeting = tk.Label(text="Content Miner v0.1")
    greeting.pack()

    content_frame = tk.Frame()
    content_label = tk.Label(master=content_frame, text="Content path:")
    content_label.grid(row=0, column=0)
    content_entry = tk.Entry(master=content_frame, width=80)
    content_entry.insert(0, read_key(CacheKey.CONTENT_PATH))
    content_entry.grid(row=0, column=1)

    content_frame.pack()

    known_words_frame = tk.Frame()
    known_words_label = tk.Label(master=known_words_frame, text="Known word list path:")
    known_words_label.grid(row=0, column=0)
    known_words_entry = tk.Entry(master=known_words_frame, width=80)
    known_words_entry.insert(0, read_key(CacheKey.KNOWN_WORDS_PATH))
    known_words_entry.grid(row=0, column=1)

    known_words_frame.pack()

    destination_frame = tk.Frame()
    destination_label = tk.Label(master=destination_frame, text="Destination path:")
    destination_label.grid(row=0, column=0)
    destination_entry = tk.Entry(master=destination_frame, width=80)
    destination_entry.insert(0, read_key(CacheKey.DESTINATION_PATH))
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
        update_key(CacheKey.CONTENT_PATH, content_entry.get())
        update_key(CacheKey.KNOWN_WORDS_PATH, known_words_entry.get())
        update_key(CacheKey.DESTINATION_PATH, destination_entry.get())

    def validate(content_path: str, known_path: str, destination_path: str, target_count: str) -> bool:
        errorMsg = ""
        makeMessage = lambda field : f"\n{field} is a required field."

        if len(content_path) == 0:
            errorMsg += makeMessage("Content path")

        if len(known_path) == 0:
            errorMsg += makeMessage("Known words path")

        if len(destination_path) == 0:
            errorMsg += makeMessage("Destination path")

        try:
            if int(target_count) < 1:
                raise ValueError
        except ValueError:
            errorMsg += "\nTarget count must be a number greater than zero."

        if len(errorMsg) > 0:
            messagebox.showerror("Validation Error", errorMsg)
            return False

        return True

    def find_sentences():
        content_path, known_path, dest_path = content_entry.get(), known_words_entry.get(), destination_entry.get()
        target_count_str = target_count.get()

        if not validate(content_path, known_path, dest_path, target_count_str):
            return

        update_cache()

        add_event, get_profile_report = profiler()

        content = load_content_file(content_path)
        known_words = load_wordlist_file(known_path)

        add_event("Loading files")

        analysed = analyse_content(content, known_words)

        add_event("Analysis")

        save_output(analysed, dest_path, bool(targets_only.get()), bool(show_freq.get()), int(target_count_str))

        add_event("Saving output")
        print(get_profile_report())

    button = tk.Button(text="Find sentences", command=find_sentences)
    button.pack()
    
    window.mainloop()