import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from lyricsgenius import Genius

GENIUS_API_TOKEN = '4yCO4ckg_wxMla96rdXXP9icX-7OAPyNoOKZHa3e4-vtHwN7NPjysSxm3FrkBseq'
genius = Genius(GENIUS_API_TOKEN)

def fetch_lyrics():
    artist_name = artist_entry.get()
    song_title = song_entry.get()

    if not artist_name or not song_title:
        messagebox.showwarning("Input Error", "Please enter both artist and song title")
        return
    try:
        song = genius.search_song(song_title, artist_name)
        if song:
            lyrics_display.delete(1.0, tk.END)
            lyrics_display.insert(tk.END, song.lyrics)
        else:
            messagebox.showinfo("No Lyrics Found", "Could not find lyrics for the specified song.")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def upload_music_file():
    file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
    if file_path:
        artist, title = get_song_info(file_path)
        artist_entry.delete(0, tk.END)
        artist_entry.insert(0, artist)
        song_entry.delete(0, tk.END)
        song_entry.insert(0, title)

def get_song_info(file_path):
    try:
        audio = MP3(file_path, ID3=EasyID3)
        artist = audio['artist'][0] if 'artist' in audio else 'Unknown'
        title = audio['title'][0] if 'title' in audio else 'Unknown'
        return artist, title
    except Exception as e:
        messagebox.showerror("Error", f"Error reading {file_path}: {e}")
        return 'Unknown', 'Unknown'

root = tk.Tk()
root.title("Lyrics Fetcher")


tk.Label(root, text="Artist Name:").grid(row=0, column=0, padx=10, pady=10)
artist_entry = tk.Entry(root, width=40)
artist_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Song Title:").grid(row=1, column=0, padx=10, pady=10)
song_entry = tk.Entry(root, width=40)
song_entry.grid(row=1, column=1, padx=10, pady=10)

upload_button = tk.Button(root, text="Upload Music File", command=upload_music_file)
upload_button.grid(row=2, column=0, columnspan=2, pady=10)

fetch_button = tk.Button(root, text="Fetch Lyrics", command=fetch_lyrics)
fetch_button.grid(row=3, column=0, columnspan=2, pady=20)

lyrics_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20)
lyrics_display.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
