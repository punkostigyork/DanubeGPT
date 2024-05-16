import tkinter as tk
from tkinter import filedialog
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(
    api_key=open('API_KEY.env').read()
)

# Function to generate the message and update the tkinter window
def generate_message(selected_options):
    prompt = f"Generate a 200 word essay about the Danube mentioning the following topics: {', '.join(selected_options)}"
    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        stream=True,
    )
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            message_text.insert(tk.END, chunk.choices[0].delta.content)
            message_text.see(tk.END)

# Function to save the content of the text widget to a file
def save_to_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if file_path:
        with open(file_path, 'w') as file:
            content = message_text.get("1.0", tk.END)
            file.write(content)

def open_start_menu():
    import StartMenu
    StartMenu.open_start_menu()

def regenerate_message(selected_options):
    message_text.delete("1.0", tk.END)
    generate_message(selected_options)

def open_chatbot_window(selected_options):
    # Create the tkinter window
    window = tk.Tk()
    window.title("OpenAI Message Generator")

    # Create a Text widget to display the message
    global message_text
    message_text = tk.Text(window, wrap='word', height=10, width=50)
    message_text.pack(padx=10, pady=10)

    # Create a button to save the content to a file
    save_button = tk.Button(window, text="Save", command=save_to_file)
    save_button.pack(pady=5)

    # Create a button to go back to the start menu
    start_menu_button = tk.Button(window, text="Start Menu", command=lambda: go_to_start_menu(window))
    start_menu_button.pack(pady=5)

    # Create a button to regenerate the text
    regenerate_button = tk.Button(window, text="Regenerate", command=lambda: regenerate_message(selected_options))
    regenerate_button.pack(pady=5)

    # Run the generate_message function when the window is ready
    window.after(100, lambda: generate_message(selected_options))

    # Run the tkinter event loop
    window.mainloop()

def go_to_start_menu(window):
    window.destroy()
    open_start_menu()
