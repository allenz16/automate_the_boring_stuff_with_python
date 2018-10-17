import os
# make a path
print(os.path.join('user', 'allen', 'document'))
# make paths
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(os.path.join(r'c:\Users\asweigart', filename))
# get current working directory
print(os.getcwd())
# change cwd
# print(os.chdir('this folder does not exist'))
# make dir
# os.makedirs(r'c:\abc\abc')
# get absolute path
print(os.path.abspath('.'))
# check whether the path is an absolute path
print(os.path.isabs('.'))
# get relative path between a path and the start
print(os.path.relpath('c:\\abc\\abc', 'c:\\'))
calcFilePath = 'c:\\Windows\\System32\\calc.exe'
# get a path's basename and dirname
print(os.path.split(calcFilePath))
# get basename
print(os.path.basename(calcFilePath))
# get dirname
print(os.path.dirname(calcFilePath))
# get a list of strings from a path
print(calcFilePath.split(os.path.sep))
# get single file size
print(os.path.getsize('c:\\Windows\\System32\\calc.exe'))
# list folder content
print(os.listdir('c:\\A'))
# find the total size of a folder
totalSize = 0
for filename in os.listdir('c:\\A'):
    totalSize = totalSize + os.path.getsize(os.path.join('c:\\A', filename))
print(totalSize)
# check whether a path exist
print(os.path.exists('c:\\A'))
# check whether it is a file
print(os.path.isfile('c:\\A'))
# check whether it is a folder
print(os.path.isdir('c:\\A'))

