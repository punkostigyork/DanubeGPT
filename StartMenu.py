import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageTk
import os

def open_selection_window():
    import SelectionWindow
    SelectionWindow.open_selection_window()

def open_start_menu():
    # Create the main window
    root = tk.Tk()
    root.title("Essay Generator")
    root.geometry("1000x700")  # Set window size to 1000x1000

    # Function to close the window
    def exit_program():
        root.destroy()

    # Function to close the window and open the selection window
    def generate_new_essay():
        root.destroy()
        open_selection_window()

    # Specify the path to your background image
    background_image_path = "budapest.png"

    # Ensure the path is correct and file exists
    if not os.path.isfile(background_image_path):
        print(f"Error: File '{background_image_path}' not found.")
        root.destroy()
        return

    # Load the background image using Pillow
    image = Image.open(background_image_path)
    image = image.resize((1000, 1000), Image.Resampling.LANCZOS)  # Resize the image to fit the window
    bg_image = ImageTk.PhotoImage(image)

    # Create a label to display the image
    background_label = Label(root, image=bg_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Create buttons with larger size
    button_font = ("Helvetica", 16)
    generate_button = Button(root, text="Generate New Essay", command=generate_new_essay, font=button_font, padx=20, pady=10)
    exit_button = Button(root, text="Exit", command=exit_program, font=button_font, padx=20, pady=10)

    # Add buttons to the window
    generate_button.place(relx=0.5, rely=0.4, anchor="center")
    exit_button.place(relx=0.5, rely=0.6, anchor="center")

    # Start the main event loop
    root.mainloop()

if __name__ == "__main__":
    open_start_menu()
