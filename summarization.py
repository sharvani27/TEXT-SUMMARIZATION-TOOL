import tkinter as tk
from tkinter import scrolledtext
import nltk
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer

# Download NLTK resources for tokenization
nltk.download('punkt')

def summarize_text(text, method="textrank", sentence_count=3):
    """
    Summarize the input text using the specified method.

    Parameters:
        text (str): The input text to summarize.
        method (str): Summarization method ('textrank' or 'lsa').
        sentence_count (int): Number of sentences in the summary.

    Returns:
        str: The summarized text.
    """
    # Parse the input text
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    
    # Choose summarization algorithm
    if method == "textrank":
        summarizer = TextRankSummarizer()
    elif method == "lsa":
        summarizer = LsaSummarizer()
    else:
        raise ValueError("Invalid summarization method. Choose 'textrank' or 'lsa'.")
    
    # Generate summary
    summary = summarizer(parser.document, sentence_count)
    return " ".join([str(sentence) for sentence in summary])

# Create a Tkinter window
window = tk.Tk()
window.title("Text Summarizer")
window.geometry("600x600")
window.configure(bg="#F9D1D1")  # Light pink background

# Adding custom fonts
font_title = ("SOUTHERN", 14, "bold")
font_button = ("SOUTHERN", 14, "bold")
font_label = ("SOUTHERN", 14)
font_text = ("SOUTHERN", 14)

# Function to handle summarization button click
def handle_summarize_click():
    # Get the input text from the user
    input_text = text_input.get("1.0", tk.END).strip()
    
    # Check if input text is empty
    if not input_text:
        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, "Please enter some text to summarize.")
        return
    
    # Get selected summarization method
    method = method_var.get()
    
    # Debugging: print the selected summarization method
    print(f"Selected Summarization Method: {method}")  # Debugging print statement
    
    # Generate the summary based on the selected method
    try:
        summary = summarize_text(input_text, method=method, sentence_count=2)
        
        # Display the summary
        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, summary)
    except ValueError as e:
        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, str(e))

# Function to handle clear button click
def handle_clear_click():
    # Clear both input and output text areas
    text_input.delete(1.0, tk.END)
    text_output.delete(1.0, tk.END)

# Create the UI elements
label_input = tk.Label(window, text="Enter Text to Summarize:", font=font_label, bg="#F9D1D1", fg="#6C4F97")
label_input.pack(pady=10)

text_input = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=50, height=10, font=font_text, bd=5, relief="groove", fg="blue", bg="#FFEBE4")
text_input.pack(pady=10)

# Dropdown for selecting summarization method
method_var = tk.StringVar(value="textrank")
label_method = tk.Label(window, text="Choose Summarization Method:", font=font_label, bg="#F9D1D1", fg="#6C4F97")
label_method.pack(pady=10)

method_dropdown = tk.OptionMenu(window, method_var, "textrank", "lsa")
method_dropdown.config(font=font_button, width=15, bg="#DFA8E4", relief="ridge")
method_dropdown.pack(pady=10)

# Summarize Button
summarize_button = tk.Button(window, text="Summarize", font=font_button, command=handle_summarize_click, fg="#FFF", bg="#6C4F97", relief="raised", bd=4)
summarize_button.pack(pady=20)

# Clear Button
clear_button = tk.Button(window, text="Clear", font=font_button, command=handle_clear_click, fg="#FFF", bg="#FF6347", relief="raised", bd=4)
clear_button.pack(pady=10)

# Output text box
label_output = tk.Label(window, text="Summary:", font=font_label, bg="#F9D1D1", fg="#6C4F97")
label_output.pack(pady=10)

text_output = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=50, height=10, font=font_text, bd=5, relief="groove", fg="green", bg="#FFEBE4")
text_output.pack(pady=10)

# Add hover effect for buttons
def on_enter(e):
    e.widget['bg'] = '#9B59B6'

def on_leave(e):
    e.widget['bg'] = '#6C4F97'

summarize_button.bind("<Enter>", on_enter)
summarize_button.bind("<Leave>", on_leave)

# Run the GUI
window.mainloop()
