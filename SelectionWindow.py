import tkinter as tk
from tkinter import messagebox

def open_start_menu():
    import StartMenu
    StartMenu.open_start_menu()

def open_chatbot_window(selected_options):
    import ChatBot
    ChatBot.open_chatbot_window(selected_options)

def open_selection_window():
    # Create the main window
    root = tk.Tk()
    root.title("Selection Window")
    root.geometry("500x500")

    # Section 1: Checkboxes with words, arranged horizontally
    section1_frame = tk.Frame(root)
    section1_frame.pack(pady=10)

    formal_var = tk.BooleanVar()
    informal_var = tk.BooleanVar()
    neutral_var = tk.BooleanVar()

    formal_checkbox = tk.Checkbutton(section1_frame, text="formal", variable=formal_var)
    informal_checkbox = tk.Checkbutton(section1_frame, text="informal", variable=informal_var)
    neutral_checkbox = tk.Checkbutton(section1_frame, text="neutral", variable=neutral_var)

    formal_checkbox.pack(side='left', padx=5)
    informal_checkbox.pack(side='left', padx=5)
    neutral_checkbox.pack(side='left', padx=5)

    # Section 2: Checkboxes with words, arranged in multiple lines
    section2_frame = tk.Frame(root)
    section2_frame.pack(pady=10)

    words = [
        "economic impact", "history", "Budapest",
        "bridges", "capitals", "fish",
        "wild life", "energetics", "culture",
        "nature", "environmental protection", "political impact"
    ]

    # Create checkboxes for each word and organize them in a grid
    word_vars = []
    for i, word in enumerate(words):
        var = tk.BooleanVar()
        word_vars.append(var)
        checkbox = tk.Checkbutton(section2_frame, text=word, variable=var)
        checkbox.grid(row=i//3, column=i%3, padx=5, pady=5, sticky='w')

    # Section 3: Buttons
    section3_frame = tk.Frame(root)
    section3_frame.pack(pady=20)

    button_frame = tk.Frame(section3_frame)
    button_frame.pack(pady=10)

    back_button = tk.Button(button_frame, text="Back", command=lambda: go_back(root))
    back_button.pack(side='left', padx=10)

    generate_button = tk.Button(button_frame, text="Generate", command=lambda: generate_action(root, words, word_vars))
    generate_button.pack(side='left', padx=10)

    # Start the main event loop
    root.mainloop()

def generate_action(root, words, word_vars):
    selected_options = [words[i] for i, var in enumerate(word_vars) if var.get()]
    if not selected_options:
        messagebox.showerror("Invalid Input", "Please select at least one topic.")
        return
    print("Selected options:", selected_options)
    root.destroy()
    open_chatbot_window(selected_options)

def go_back(root):
    root.destroy()
    open_start_menu()

if __name__ == "__main__":
    open_selection_window()
