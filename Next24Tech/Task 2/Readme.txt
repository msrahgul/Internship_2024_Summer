Task 2
Building a Chatbot Using Python: Your next task involves building a chatbot using Python. You will explore various libraries and techniques to develop a responsive and interactive chatbot that can engage with users effectively.


Welcome to Cricket Bot! This application is a simple chatbot designed to answer cricket-related questions. It uses a fuzzy string matching algorithm to find the best possible answer from a predefined set of question-answer pairs.

## Features

- **User-Friendly Interface**: A graphical user interface (GUI) built with `tkinter`.
- **Fuzzy Matching**: Utilizes `fuzzywuzzy` for matching user queries to the closest possible predefined questions.
- **Logging**: Implements logging to track user interactions and errors.
- **Chat History Management**: Allows users to clear the chat history.
- **Suggestions**: Provides suggestions for similar questions if an exact match isn't found.

## Usage

1. **Run the application**:
    ```sh
    python cricket_bot.py
    ```

2. **Interact with the bot**:
    - Type your cricket-related questions into the input field and press Enter or click the "Send" button.
    - To clear the chat history, click the "Clear" button.
    - To exit the application, type `exit` and press Enter.

## Code Overview

### Modules

- **tkinter**: Used for creating the GUI.
    - `tk`: Main module for the GUI.
    - `scrolledtext`: Provides a text area with scrollbars.
    - `messagebox`: Displays message boxes.
- **fuzzywuzzy**: Used for fuzzy string matching.
- **logging**: Standard Python module for logging events.

### Functions and Classes

1. **read_training_data(file_path)**:
    - Reads question-answer pairs from a file and returns them as a dictionary.

2. **CricketBotApp**:
    - Main class for the application.
    - Initializes the GUI and handles user interactions.
    - **display_message(sender, message)**: Displays messages in the chat.
    - **process_input(event=None)**: Processes user input and finds the best matching response.
    - **get_suggestions(user_message)**: Provides suggestions for similar questions.
    - **clear_chat()**: Clears the chat history.

### Logging

- Logs user inputs, bot responses, and any errors to `cricket_bot.log`.

## Example `cricket_data.txt`

```
What is the highest score in cricket? 400 by Brian Lara.
Who won the 2019 Cricket World Cup? England.
Who has the most wickets in Test cricket? Muttiah Muralitharan with 800 wickets.
```

## Contributing

Feel free to contribute to this project by creating a pull request or opening an issue on GitHub.

