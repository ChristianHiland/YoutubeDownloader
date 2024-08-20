# Importing Needed Modules.
import yt_dlp
import os

# Music Downloading FUNC
def MusicDownload(url, SAVE_PATH_MUS):
    ydl_opts = {'outtmpl': f'{SAVE_PATH_MUS}/%(title)s.%(ext)s', 'format': 'bestaudio/best',}
    # Downloading Music File
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
# Video Downloading FUNC
def VideoDownload(url, SAVE_PATH_VID):
    ydl_opts = {'outtmpl': f'{SAVE_PATH_VID}/%(title)s.%(ext)s', 'format': 'bestvideo+bestaudio/best',}
    # Downloading Video File
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
# Title Downloading FUNC
def VideoTitle(url):
    ydl_opts = { 'quiet': True, 'skip_download': True, 'force_generic_extractor': True }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        return info_dict.get('title', 'No title found')

def DownloadModeCTL(URL_List, Mode:str="video", Type:str="single", Save_Path:str="Download", PastDownloadsDA:dict="IDK"):
    if Mode.lower() == str("video"):
        print("|||||| Video Mode ||||||")
        if Type.lower() == str("single"):
            VideoDownload(URL_List[0], Save_Path)
            PastDownloadsDA.update({VideoTitle(URL_List[0]): URL_List[0]})
        elif Type.lower() == str("many"):
            for i in URL_List:
                VideoDownload(i, Save_Path)
                PastDownloadsDA.update({VideoTitle(URL_List[i]): URL_List[i]})
    elif Mode.Lower() == str("music"):
        print("|||||| Music Mode ||||||")
        if Type.lower() == str("single"):
            MusicDownload(URL_List[0], Save_Path)
            PastDownloadsDA.update({VideoTitle(URL_List[0]): URL_List[0]})
        elif Type.lower() == str("many"):
            for i in URL_List:
                MusicDownload(i, Save_Path)
                PastDownloadsDA.update({VideoTitle(URL_List[i]): URL_List[i]})

    # Returning The New DICT for Past Downloads
    return PastDownloadsDA