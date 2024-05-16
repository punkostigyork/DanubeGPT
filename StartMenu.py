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
    bg_image = ImageTk.PhotoImage(image)

    # Get the image dimensions
    img_width, img_height = image.size

    # Set the window size to match the image
    root.geometry(f"{img_width}x{img_height}")

    # Create a label to display the image
    background_label = Label(root, image=bg_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Create buttons
    generate_button = Button(root, text="Generate New Essay", command=generate_new_essay)
    exit_button = Button(root, text="Exit", command=exit_program)

    # Add buttons to the window
    generate_button.place(relx=0.5, rely=0.5, anchor="center")
    exit_button.place(relx=0.5, rely=0.55, anchor="center")

    # Start the main event loop
    root.mainloop()

if __name__ == "__main__":
    open_start_menu()
