import os
for folderName, subFolders, fileNames in os.walk('c:\\A'):
    print('The current folder is ' + folderName)
    for subFolder in subFolders:
        print('subFolder of ' + folderName + ': ' + subFolder)
    for fileName in fileNames:
        print('File inside ' + folderName + ': ' + fileName)

    print('')
