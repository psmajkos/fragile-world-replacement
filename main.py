from tkinter import *
import json
from tkinter import Toplevel
import tkinter as tk
def add():
    data = {
        "psychiatrist": '[REDACTED]'
    }
    with open('words.json', 'w') as f:
        json.dump(data, f)


    root =tk.Toplevel()
    word = StringVar()
    word_label = Label(root, text="Enter word to replace")
    word_label.pack()
    word_entry = Entry(root, textvariable=word)
    word_entry.pack()

    def insert():
        # Read the contents of the JSON file
        with open('words.json', 'r') as f:
            data = json.load(f)

        # Add a new entry to the data dictionary
        data[word.get()] = '[REDACTED]'

        # Write the updated data back to the file
        with open('words.json', 'w') as f:
            json.dump(data, f)

        # Clear the Entry widget
        word_entry.delete(0, END)

    root.bind('<Return>', lambda event=None: insert())
    apply_button = Button(root, command=insert, text='Insert')
    apply_button.pack()

    root.mainloop()

def main_app():
    root = Tk()
    root.attributes('-fullscreen', True)

    with open('words.json', 'r') as f:
        words = json.load(f)

    input_text_lbl = Label(root, text="Input text")
    input_text_lbl.pack()
    input_text = Text(root, width=400, height=25)
    input_text.focus()
    input_text.pack()

    def replace():
        # Read the contents of the JSON file to get the latest words
        with open('words.json', 'r') as f:
            words = json.load(f)

        text = input_text.get("1.0", END)
        for word in words:
            text = text.replace(word, words[word])
        replaced_text.delete("1.0", END)
        replaced_text.insert("1.0", text)
        if delete.get():
            input_text.delete("1.0", END)

    root.bind('<Return>', lambda event=None: replace())

    def toggle_delete():
        # Update the state of the delete variable
        delete.set(not delete.get())

    replaced_text_lbl = Label(root, text="Replaced text")
    replaced_text_lbl.pack()
    replaced_text = Text(root, width=400, height=25)
    replaced_text.pack()

    apply_button = Button(root, text="Apply", command=replace)
    apply_button.pack()

    delete = BooleanVar()

    delete_checkbutton = Checkbutton(root, text = "Delete inputed text", variable = delete, \
                    onvalue = 1, offvalue = 0, height=5, \
                    width = 20)
    delete_checkbutton.pack()

    add_word = Button(root, text="Add words", command=add)
    add_word.pack()

    root.mainloop()
main_app()