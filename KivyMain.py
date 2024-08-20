# Importing Needed Modules
from kivy.uix.gridlayout import GridLayout      # Kivy Modules
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.app import App
import Modules                                  # Self Made Modules

import yt_dlp

import sys                                      # System Modules
import json
import os

# Init Vars.
SAVE_PATH_VID = "VideoDownloads/"
SAVE_PATH_MUS = "MusicDownloads/"

# File & Data
PastDownloadFile = "Data/PastDownloads.json"
YoutubeLinksFile = "YoutubeLinks.json"

# Fake Vars
FAKE_DICT = {
    "Fake": "FAKE"
}

def FileInit():
    # Making Past Download JSON if not There.
    if os.path.exists(PastDownloadFile) != True:
        defalut = {
            "Test": "Test"
        }
        with open(PastDownloadFile, "x") as PastDownloadsOP:
            json.dump(defalut, PastDownloadsOP)
    # Opening Past Downloads JSON
    with open(PastDownloadFile, "r") as PastDownloadsOP:
        return json.load(PastDownloadsOP)


class YoutubeDownloader(App):
    def build(self):
        # Setting Window Style & Layout
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.9)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        # Widgets & Objects

        # Label (Title)
        self.Title_Label = Label(text="YouTube Downloader (PC Edition)", font_size=30)
        self.window.add_widget(self.Title_Label)

        # Label (Title)
        self.Body_Label = Label(text="Enter YouTube URL, and Press Download", font_size=20)
        self.window.add_widget(self.Body_Label)

        # URL TextInput
        self.Url_Input = TextInput(multiline=False, padding_y=(12,12), size_hint=(1,0.23), font_size=20)
        self.window.add_widget(self.Url_Input)

        # Download Button
        self.Download_Button = Button(text="Download", size_hint=(1,0.3), bold=True)
        self.Download_Button.bind(on_press=self.VideoDownload)
        self.window.add_widget(self.Download_Button)

        # End Of Section
        return self.window
    
    # Video Downloading FUNC
    def VideoDownload(self, instence):
        # Telling User
        self.Body_Label.text = str("Downloading Please Wait...")
        # Downloading
        ydl_opts = {'outtmpl': f'{SAVE_PATH_VID}/%(title)s.%(ext)s', 'format': 'bestvideo+bestaudio/best',}
        # Downloading Video File
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.Url_Input.text])
        # Telling User
        self.Body_Label.text = str(f"Video Downloaded at '{SAVE_PATH_VID}'")

if __name__ == "__main__":
    YoutubeDownloader().run()