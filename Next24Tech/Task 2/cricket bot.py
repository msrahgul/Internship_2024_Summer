import tkinter as tk
from tkinter import scrolledtext, messagebox
from fuzzywuzzy import process
import logging

# Initialize logging
logging.basicConfig(filename='cricket_bot.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def read_training_data(file_path):
    qa_pairs = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                if line.strip():
                    q, a = line.strip().split('? ')
                    qa_pairs[q + '?'] = a  # Include the question mark in the key
    except Exception as e:
        logging.error(f"Error reading training data: {e}")
    return qa_pairs

class CricketBotApp(tk.Tk):
    def __init__(self, training_data):
        super().__init__()
        self.training_data = training_data
        self.title("Cricket Bot")
        self.geometry("600x500")

        self.chat_display = scrolledtext.ScrolledText(self, wrap=tk.WORD, state='disabled', width=70, height=25)
        self.chat_display.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        self.user_input = tk.Entry(self, width=50)
        self.user_input.grid(row=1, column=0, padx=10, pady=10)
        self.user_input.bind("<Return>", self.process_input)

        self.send_button = tk.Button(self, text="Send", command=self.process_input)
        self.send_button.grid(row=1, column=1, padx=10, pady=10)

        self.clear_button = tk.Button(self, text="Clear", command=self.clear_chat)
        self.clear_button.grid(row=1, column=2, padx=10, pady=10)

        self.display_message("Cricket Bot", "Welcome to Cricket Bot! Ask any cricket-related question or type 'exit' to quit.")

    def display_message(self, sender, message):
        self.chat_display.configure(state='normal')
        self.chat_display.insert(tk.END, f"{sender}: {message}\n")
        self.chat_display.configure(state='disabled')
        self.chat_display.see(tk.END)
        logging.info(f"{sender}: {message}")

    def process_input(self, event=None):
        user_message = self.user_input.get().strip().lower()
        self.user_input.delete(0, tk.END)

        if user_message:
            self.display_message("You", user_message)
            logging.info(f"User input: {user_message}")

            if user_message == 'exit':
                self.display_message("Cricket Bot", "Goodbye!")
                self.after(2000, self.destroy)  # Close the application after 2 seconds
                return

            best_match, score = process.extractOne(user_message, self.training_data.keys(), score_cutoff=60)
            if best_match:
                self.display_message("Cricket Bot", self.training_data[best_match])
            else:
                self.display_message("Cricket Bot", "Sorry, I don't have an answer for that.")
                suggestions = self.get_suggestions(user_message)
                if suggestions:
                    self.display_message("Cricket Bot", "Did you mean:\n" + "\n".join(suggestions))

    def get_suggestions(self, user_message):
        matches = process.extract(user_message, self.training_data.keys(), limit=3)
        suggestions = [match[0] for match in matches if match[1] >= 50]
        return suggestions

    def clear_chat(self):
        self.chat_display.configure(state='normal')
        self.chat_display.delete(1.0, tk.END)
        self.chat_display.configure(state='disabled')
        self.display_message("Cricket Bot", "Chat cleared.")

if __name__ == "__main__":
    training_file = 'cricket_data.txt'
    data = read_training_data(training_file)
    app = CricketBotApp(data)
    app.mainloop()
