Task 3
 Creating GUI to Extract Lyrics from Songs Using Python: Your final task is to design a graphical user interface (GUI) application that can extract lyrics from songs using Python. You will integrate APIs or web scraping techniques to fetch lyrics and display them on the interface.

# Lyrics Fetcher

Lyrics Fetcher is a Python application that retrieves song lyrics based on the artist and song title provided by the user. It offers a simple and user-friendly graphical user interface (GUI) built with `tkinter`.

## Features

- **User-Friendly Interface**: The GUI is built using `tkinter` and provides an easy way to input song information and display lyrics.
- **Music File Upload**: Allows users to upload MP3 files and automatically extracts the artist and song title from the file metadata.
- **Lyrics Retrieval**: Fetches lyrics using the Genius API.
- **Error Handling**: Provides warnings and error messages for invalid inputs or issues during the lyrics fetching process.

## Requirements

- Python 3.x
- `tkinter` (usually included with Python installations)
- `mutagen` library
- `lyricsgenius` library

## Installation

1. **Install the required Python libraries**:
    pip install mutagen lyricsgenius   

## Usage

1. **Interact with the application**:
    - **Artist Name**: Enter the artist's name in the provided entry field.
    - **Song Title**: Enter the song title in the provided entry field.
    - **Upload Music File**: Click the "Upload Music File" button to select an MP3 file from your computer. The application will extract the artist and title information from the file.
    - **Fetch Lyrics**: Click the "Fetch Lyrics" button to retrieve the lyrics for the specified song. The lyrics will be displayed in the text area.

## Code Overview

### Modules

- **tkinter**: Used for creating the GUI.
  - `tk`: Main module for the GUI.
  - `filedialog`: Provides file dialog windows.
  - `messagebox`: Displays message boxes.
  - `scrolledtext`: Provides a text area with scrollbars.
- **mutagen**: Used for reading metadata from MP3 files.
  - `easyid3`: Reads ID3 tags.
  - `MP3`: Handles MP3 file format.
- **lyricsgenius**: Used for fetching lyrics from Genius.

### Functions

1. **fetch_lyrics()**:
    - Retrieves and displays lyrics based on the artist and song title input by the user.

2. **upload_music_file()**:
    - Opens a file dialog for the user to select an MP3 file.
    - Extracts and displays the artist and song title from the file's metadata.

3. **get_song_info(file_path)**:
    - Reads the artist and title from the MP3 file's metadata.

## Contributing

Feel free to contribute to this project by creating a pull request or opening an issue on GitHub.

