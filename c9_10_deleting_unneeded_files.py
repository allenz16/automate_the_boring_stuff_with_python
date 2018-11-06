import os
import send2trash


def delete_big_files(folder):
    for folderName, subFolders, fileNames in os.walk(folder):
        for fileName in fileNames:
            if os.path.getsize(folderName + os.sep + fileName) > 5242880:
                send2trash.send2trash(folderName + os.sep + fileName)


delete_big_files('c:\\C')


