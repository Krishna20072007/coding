import os
import pygame
import random
from tkinter import *
from tkinter import filedialog
from mutagen.mp3 import MP3
import time

# Initialize Pygame
pygame.init()

# Create a MusicPlayer class
class MusicPlayer:
    def __init__(self):
        self.playlist = []  # List to store the playlist
        self.current_index = 0  # Index of the current song
        self.repeat = False  # Flag for repeat mode
        self.shuffle = False  # Flag for shuffle mode

    def add_song(self, folder_path):
        # Get all files from the folder
        files = os.listdir(folder_path)

        # Filter and add compatible audio files to the playlist
        for file in files:
            if file.endswith(".mp3") or file.endswith(".wav"):
                song_path = os.path.join(folder_path, file)
                self.playlist.append(song_path)

    def play(self):
        # Load the current song
        current_song = pygame.mixer.music.load(self.playlist[self.current_index])

        # Play the song
        pygame.mixer.music.play()

    def stop(self):
        pygame.mixer.music.stop()

    def next(self):
        # Stop the current song
        pygame.mixer.music.stop()

        # Update the current index
        if self.shuffle:
            self.current_index = random.randint(0, len(self.playlist) - 1)
        else:
            self.current_index = (self.current_index + 1) % len(self.playlist)

        # Play the next song
        self.play()

    def previous(self):
        # Stop the current song
        pygame.mixer.music.stop()

        # Update the current index
        self.current_index = (self.current_index - 1) % len(self.playlist)

        # Play the previous song
        self.play()

    def toggle_repeat(self):
        self.repeat = not self.repeat
        pygame.mixer.music.set_repeat(-1 if self.repeat else 0)

    def toggle_shuffle(self):
        self.shuffle = not self.shuffle

    def get_current_song_duration(self):
        song_path = self.playlist[self.current_index]
        audio = MP3(song_path)
        return audio.info.length

    def print_playlist(self):
        print("Playlist:")
        for i, song in enumerate(self.playlist):
            print(f"{i+1}. {song}")


# Create an instance of the MusicPlayer class
player = MusicPlayer()

# Tkinter GUI
root = Tk()
root.title("Music Player")

# Function to open a folder and add songs to the playlist
def add_folder():
    folder_path = filedialog.askdirectory()
    player.add_song(folder_path)
    playlist.delete(0, END)
    for song in player.playlist:
        playlist.insert(END, song)

# Function to play the selected song from the playlist
def play_song():
    selection = playlist.curselection()
    if selection:
        index = int(selection[0])
        player.current_index = index
        player.play()
        update_song_details()

# Function to stop the current song
def stop_song():
    player.stop()
    song_label.config(text="")

# Function to play the next song
def next_song():
    player.next()
    update_song_details()

# Function to play the previous song
def previous_song():
    player.previous()
    update_song_details()

# Function to toggle repeat mode
def toggle_repeat():
    player.toggle_repeat()

# Function to toggle shuffle mode
def toggle_shuffle():
    player.toggle_shuffle()

# Function to update the song details label
def update_song_details():
    current_song = player.playlist[player.current_index]
    song_label.config(text=f"Current Song: {os.path.basename(current_song)}")
    duration = player.get_current_song_duration()
    duration_bar.config(to=duration)
    duration_bar.set(0)

# Function to update the duration bar
def update_duration():
    if pygame.mixer.music.get_busy():
        current_time = pygame.mixer.music.get_pos() / 1000  # Convert milliseconds to seconds
        duration_bar.set(current_time)
    root.after(1000, update_duration)

# Playlist
playlist = Listbox(root)
playlist.pack()

# Buttons
add_folder_btn = Button(root, text="Add Folder", command=add_folder)
add_folder_btn.pack()

play_btn = Button(root, text="Play", command=play_song)
play_btn.pack()

stop_btn = Button(root, text="Stop", command=stop_song)
stop_btn.pack()

next_btn = Button(root, text="Next", command=next_song)
next_btn.pack()

previous_btn = Button(root, text="Previous", command=previous_song)
previous_btn.pack()

repeat_btn = Button(root, text="Repeat", command=toggle_repeat)
repeat_btn.pack()

shuffle_btn = Button(root, text="Shuffle", command=toggle_shuffle)
shuffle_btn.pack()

# Current Song Label
song_label = Label(root)
song_label.pack()

# Duration Bar
duration_bar = Scale(root, from_=0, to=100, orient=HORIZONTAL)
duration_bar.pack()

# Update duration bar
update_duration()

# Run the Tkinter event loop
root.mainloop()

# Quit Pygame
pygame.quit()
