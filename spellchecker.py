import tkinter as tk
from tkinter import messagebox
from autocorrect import Speller

# Create the Tkinter window
window = tk.Tk()
window.title("Autocorrect")
window.geometry("800x600")  # Increased window size

# Set the theme color
window.configure(bg="lightblue")

# Initialize autocorrect spell checker
spell = Speller(lang='en')

# Function to perform autocorrection
def autocorrect():
    text = input_text.get("1.0", "end-1c")
    corrected_text = spell(text)
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    output_text.insert("1.0", "The corrected text:\n" + corrected_text)
    output_text.config(state=tk.DISABLED)
    messagebox.showinfo("Autocorrect", "Autocorrection completed!")  # Show message after completion

# Function to manually trigger spell check
def spell_check():
    text = input_text.get("1.0", "end-1c")
    misspelled_words = [word for word in text.split() if not spell(word)]
    if misspelled_words:
        messagebox.showinfo("Misspelled Words", f"Misspelled words: {', '.join(misspelled_words)}")
    else:
        messagebox.showinfo("Spell Check", "No misspelled words found.")

# Function to clear the input field
def clear_input():
    input_text.delete("1.0", tk.END)

# Function to save the corrected text to a file
def save_text():
    text = output_text.get("1.0", "end-1c")
    with open("corrected_text.txt", "w") as file:
        file.write(text)
    messagebox.showinfo("Save", "Corrected text saved to 'corrected_text.txt'.")

# Function to update character count
def update_char_count(event):
    text = input_text.get("1.0", "end-1c")
    char_count_label.config(text=f"Character count: {len(text)}")

# Function to update word count
def update_word_count(event):
    text = input_text.get("1.0", "end-1c")
    words = text.split()
    word_count_label.config(text=f"Word count: {len(words)}")

# Create input field with prompt text
input_text = tk.Text(window, width=60, height=5, font=("Arial", 12))
input_text.insert("1.0", "Enter text here...")
input_text.bind("<FocusIn>", lambda event: input_text.delete("1.0", "end-1c"))
input_text.bind("<FocusOut>", lambda event: input_text.insert("1.0", "Enter text here..."))
input_text.bind("<Key>", update_char_count)
input_text.bind("<KeyRelease>", update_word_count)
input_text.pack(pady=5)

# Create button to trigger autocorrection
autocorrect_button = tk.Button(window, text="Autocorrect", command=autocorrect, bg="blue", fg="white", font=("Arial", 12))
autocorrect_button.pack(pady=5)

# Create button to manually trigger spell check
spell_check_button = tk.Button(window, text="Spell Check", command=spell_check, bg="green", fg="white", font=("Arial", 12))
spell_check_button.pack(pady=5)

# Create button to clear the input field
clear_button = tk.Button(window, text="Clear Input", command=clear_input, bg="red", fg="white", font=("Arial", 12))
clear_button.pack(pady=5)

# Create button to save the corrected text
save_button = tk.Button(window, text="Save", command=save_text, bg="orange", fg="white", font=("Arial", 12))
save_button.pack(pady=5)

# Create output text widget to display corrected text
output_text = tk.Text(window, width=60, height=5, font=("Arial", 12), state=tk.DISABLED)
output_text.pack(pady=5)

# Create label to display character count
char_count_label = tk.Label(window, text="Character count: 0", font=("Arial", 10), bg="lightblue")
char_count_label.pack(pady=5)

# Create label to display word count
word_count_label = tk.Label(window, text="Word count: 0", font=("Arial", 10), bg="lightblue")
word_count_label.pack(pady=5)

# Run the Tkinter event loop
window.mainloop()