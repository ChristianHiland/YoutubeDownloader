# Importing Needed Modules
import Modules                      # Self Made Modules

import sys                          # System Modules
import json
import os

# Init Vars.
SAVE_PATH_VID = "VideoDownloads/"
SAVE_PATH_MUS = "MusicDownloads/"

# File & Data
PastDownloadFile = "Data/PastDownloads.json"
YoutubeLinksFile = "YoutubeLinks.json"

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

if __name__ == "__main__":
    # Video List
    with open(YoutubeLinksFile, "r") as YoutubeLinksOP:
        video_list = json.load(YoutubeLinksOP)

    # Starting & Checking Files
    PastDownloadsDA = FileInit()

    # Checking for User ARGS
    if sys.argv[1].lower() == str("download"):
        if sys.argv[2].lower() == str("video"):
            if sys.argv[3].lower() == str("single"):
                PastDownloadsDA_NEW = Modules.Download(video_list, "video", "single", SAVE_PATH_VID, PastDownloadsDA)
            elif sys.argv[3].lower() == str("many"):
                PastDownloadsDA_NEW = Modules.Download(sys.argv[4], "video", "many", SAVE_PATH_VID, PastDownloadsDA)
        elif sys.argv[2].lower() == str(""):
            if sys.argv[3].lower() == str("single"):
                PastDownloadsDA_NEW = Modules.Download(sys.argv[4], "music", "single", SAVE_PATH_MUS, PastDownloadsDA)
            elif sys.argv[3].lower() == str("many"):
                PastDownloadsDA_NEW = Modules.Download(sys.argv[4], "music", "many", SAVE_PATH_MUS, PastDownloadsDA)
    elif sys.argv[1].lower() == str("help"):
        Modules.Help_Print()


    # F.I.N. With Writing all the things downloaded
    with open(PastDownloadFile, "w") as PastDownloadOP:
        try:
            json.dump(PastDownloadsDA_NEW, PastDownloadOP, indent=4)
        except NameError:
            json.dump(PastDownloadsDA, PastDownloadOP, indent=4)