import tkinter as tk
import openai

# Replace with your actual OpenAI API key
openai.api_key = 'sk-proj-iccDsPEy4XYvSyRvyrHfT3BlbkFJmsrQFNdSl1mPMFCEOZNo'

def open_chatbot_window(selected_options):
    # Create the main window
    root = tk.Tk()
    root.title("Generated Text")
    root.geometry("600x400")

    # Function to generate text using OpenAI GPT
    def generate_text():
        prompt = f"Generate an essay on the following topics: {', '.join(selected_options)} with a minimum of 500 words."
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use "gpt-4" if you have access
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=2048,
            temperature=0.7
        )
        generated_text = response['choices'][0]['message']['content'].strip()
        text_widget.insert(tk.END, generated_text)

    # Create a Text widget to display the generated text
    text_widget = tk.Text(root, wrap=tk.WORD)
    text_widget.pack(expand=True, fill=tk.BOTH)

    # Generate the text and display it
    generate_text()

    root.mainloop()

if __name__ == "__main__":
    open_chatbot_window(["example"])
