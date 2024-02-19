import tkinter as tk
from tkinter import messagebox
from autocorrect import Speller


window = tk.Tk()
window.title("Autocorrect")
window.geometry("800x600")  


window.configure(bg="lightblue")

spell = Speller(lang='en')


def autocorrect():
    text = input_text.get("1.0", "end-1c")
    corrected_text = spell(text)
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    output_text.insert("1.0", "The corrected text:\n" + corrected_text)
    output_text.config(state=tk.DISABLED)
    messagebox.showinfo("Autocorrect", "Autocorrection completed!")  


def spell_check():
    text = input_text.get("1.0", "end-1c")
    misspelled_words = [word for word in text.split() if not spell(word)]
    if misspelled_words:
        messagebox.showinfo("Misspelled Words", f"Misspelled words: {', '.join(misspelled_words)}")
    else:
        messagebox.showinfo("Spell Check", "No misspelled words found.")
def clear_input():
    input_text.delete("1.0", tk.END)


def save_text():
    text = output_text.get("1.0", "end-1c")
    with open("corrected_text.txt", "w") as file:
        file.write(text)
    messagebox.showinfo("Save", "Corrected text saved to 'corrected_text.txt'.")


def update_char_count(event):
    text = input_text.get("1.0", "end-1c")
    char_count_label.config(text=f"Character count: {len(text)}")


def update_word_count(event):
    text = input_text.get("1.0", "end-1c")
    words = text.split()
    word_count_label.config(text=f"Word count: {len(words)}")


input_text = tk.Text(window, width=60, height=5, font=("Arial", 12))
input_text.insert("1.0", "Enter text here...")
input_text.bind("<FocusIn>", lambda event: input_text.delete("1.0", "end-1c"))
input_text.bind("<FocusOut>", lambda event: input_text.insert("1.0", "Enter text here..."))
input_text.bind("<Key>", update_char_count)
input_text.bind("<KeyRelease>", update_word_count)
input_text.pack(pady=5)


autocorrect_button = tk.Button(window, text="Autocorrect", command=autocorrect, bg="blue", fg="white", font=("Arial", 12))
autocorrect_button.pack(pady=5)


spell_check_button = tk.Button(window, text="Spell Check", command=spell_check, bg="green", fg="white", font=("Arial", 12))
spell_check_button.pack(pady=5)


clear_button = tk.Button(window, text="Clear Input", command=clear_input, bg="red", fg="white", font=("Arial", 12))
clear_button.pack(pady=5)
save_button = tk.Button(window, text="Save", command=save_text, bg="orange", fg="white", font=("Arial", 12))
save_button.pack(pady=5)


output_text = tk.Text(window, width=60, height=5, font=("Arial", 12), state=tk.DISABLED)
output_text.pack(pady=5)


char_count_label = tk.Label(window, text="Character count: 0", font=("Arial", 10), bg="lightblue")
char_count_label.pack(pady=5)


word_count_label = tk.Label(window, text="Word count: 0", font=("Arial", 10), bg="lightblue")
word_count_label.pack(pady=5)


window.mainloop()
