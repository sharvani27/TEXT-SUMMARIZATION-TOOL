# TEXT-SUMMARIZATION-TOOL

*COMPANY*: CODETECH IT SOLUTION

*NAME*: SHARVANI SURAJ MAHADIK

*INTERN ID*:CT08LKR

*DOMAIN*:AI

*DURATION*:4 WEEKS 

*MENTOR*: NEELA SANTOSH

*DESCRIPTION*:The Text Summarizer application created with Python and Tkinter is designed to summarize long text into a shorter version using natural language processing (NLP) techniques. The code incorporates two popular text summarization methods: TextRank and LSA (Latent Semantic Analysis). The goal of the application is to allow users to input text, choose a summarization method, and receive a concise summary.
This Text Summarizer application demonstrates a simple, interactive tool for summarizing text using NLP methods. It makes text summarization more accessible to non-programmers by providing a clean and intuitive interface. The use of Sumy for summarization and Tkinter for GUI development ensures that the application is both effective and easy to use. Whether for academic purposes, business, or personal use, this app can save time by providing concise summaries of lengthy content.

*OVERVIEW*:This application uses Tkinter for the graphical user interface (GUI), and Sumy along with NLTK for performing the text summarization. The application is capable of handling text summarization through two different methods and providing the summarized text back to the user. It provides a user-friendly interface that allows users to input text, select the summarization method, and view the output summary.

*Import Required Libraries*:
import tkinter as tk
from tkinter import scrolledtext
import nltk
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer

*LIBRARIES DESCRIPTION*:
tkinter: The core library for creating the GUI.
scrolledtext: A widget in Tkinter that allows the creation of a text area with scroll functionality.
nltk: The Natural Language Toolkit, used here to download a tokenizer for splitting text into sentences.
sumy: A library for text summarization. We use PlaintextParser to parse text and two summarizers, LsaSummarizer and TextRankSummarizer, to generate summaries.

*Download Necessary NLTK Resources*:
nltk.download('punkt')
This line downloads the punkt tokenizer from NLTK, which is essential for breaking the input text into sentences.
Summarization Logic (The summarize_text function):
def summarize_text(text, method="textrank", sentence_count=3):
    ...
This function is responsible for summarizing the input text based on the selected method:

Text Parsing: The PlaintextParser.from_string function parses the input text and prepares it for processing by the summarization methods.
Summarization Methods:
If the method selected is "textrank", the TextRankSummarizer() is used.
If the method is "lsa", the LsaSummarizer() is used.
Returning the Summary: After generating the summary, the sentences are joined together and returned as a string.

*Setting Fonts for the GUI*:
font_title = ("SOUTHERN", 14, "bold")
font_button = ("SOUTHERN", 14, "bold")
font_label = ("SOUTHERN", 14)
font_text = ("SOUTHERN", 14)
Custom fonts are defined to ensure consistency in the appearance of the GUI. These fonts are applied to labels, buttons, and text areas in the application.

*Building the User Interface*:
Text Input Area: A scrollable text area (text_input) is provided where users can paste or type the text they want to summarize.
Summarization Method Dropdown: A dropdown menu allows users to choose between "TextRank" or "LSA" as the summarization method. The default method is "TextRank".
Summarize Button: When clicked, this button triggers the summarization process. The text from the input area is passed to the summarize_text function, and the result is displayed.
Clear Button: Clears both the input and output text areas.

*Event Handlers for Buttons*:
def handle_summarize_click():
def handle_clear_click():
Summarize Button Handler:
The handle_summarize_click function is triggered when the user clicks the "Summarize" button.
It retrieves the text from the input area, checks if the text is empty, and then calls the summarize_text function to generate a summary.
The summary is then displayed in the output text area.
Clear Button Handler:
The handle_clear_click function clears both the input and output text areas, allowing the user to start fresh.

*Running the GUI*:
window.mainloop()
This line starts the Tkinter event loop, which keeps the application running and responsive to user input until the window is closed.

*OUTPUT*:

![Image](https://github.com/user-attachments/assets/9cd41c66-cdcf-4dc3-8b7d-e9f655d96bb7)

![Image](https://github.com/user-attachments/assets/38fc9302-5cf0-45d0-acf4-8b19bfad8418)



