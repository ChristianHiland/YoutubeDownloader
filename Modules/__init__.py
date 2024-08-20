# Importing Needed Modules
# Module Import Check
try:
    import yt_dlp
except ImportError:
    print("{ImportError}! Failed To Import 'yt_dlp'! Please Install With 'PIP'\n(Note: ffmeg may need to be installed!)")

try:
    from rich.tree import Tree
    from rich import print as PRINT
except ImportError:
        print("{ImportError}! Failed To Import 'rich'! Please Install With 'PIP'")

from Modules.Download import DownloadModeCTL as Download
from Modules.ARGs_Options import Help_Print

