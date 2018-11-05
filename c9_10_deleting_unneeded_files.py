import os


def delete_big_files(folder):
    for folderName, subFolders, fileNames in os.walk(folder):
        for fileName in fileNames:
            if os.path.getsize(folderName + os.sep + fileName) > 104857600:

