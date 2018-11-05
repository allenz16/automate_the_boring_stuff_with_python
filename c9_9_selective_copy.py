import os
import shutil


def pdf_copy(folder, targetFolder):
    for folderName, subFolders, fileNames in os.walk(folder):
        for fileName in fileNames:
            if fileName.endswith('.pdf'):
                print(os.path.abspath(folderName + os.sep + fileName))
                shutil.copy(os.path.abspath(folderName + os.sep + fileName), targetFolder)


pdf_copy('c:\\A', 'c:\\B')
