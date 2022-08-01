import tkinter as tk


def start_gui():
    window = tk.Tk()

    greeting = tk.Label(text="Content Miner v0.1")
    greeting.pack()

    content_frame = tk.Frame()
    content_label = tk.Label(master=content_frame, text="Content path:")
    content_label.grid(row=0, column=0)
    content_entry = tk.Entry(master=content_frame, width=80)
    content_entry.grid(row=0, column=1)

    content_frame.pack()

    known_words_frame = tk.Frame()
    known_words_label = tk.Label(master=known_words_frame, text="Known word list path:")
    known_words_label.grid(row=0, column=0)
    known_words_entry = tk.Entry(master=known_words_frame, width=80)
    known_words_entry.grid(row=0, column=1)

    known_words_frame.pack()

    destination_frame = tk.Frame()
    destination_label = tk.Label(master=destination_frame, text="Destination path:")
    destination_label.grid(row=0, column=0)
    destination_entry = tk.Entry(master=destination_frame, width=80)
    destination_entry.grid(row=0, column=1)

    destination_frame.pack()

    button = tk.Button(text="Find sentences")
    button.pack()
    
    window.mainloop()