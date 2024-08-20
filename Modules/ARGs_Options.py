from Modules import Tree            # Rich Modules
from Modules import PRINT

def Help_Print():
    #print("||||||||||||||||| Help |||||||||||||||||||\n||")
    #print("|| Download 'Format Type' 'URL Format'  ||")
    #print("|| EX: download video single 'URL'      ||\n||")
    #print("||||||||||||||||||||||||||||||||||||||||||")

    tree = Tree("Help")
    DownloadCMD_Tree = tree.add("Download")
    DownloadCMD_F_Tree = DownloadCMD_Tree.add("Format Type")
    DownloadCMD_F_Tree.add("URL")
    treeEX = tree.add("EX:")
    DownloadCMD_EX = treeEX.add("download video single 'URL'")

    PRINT(tree)