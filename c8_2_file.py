# open a file
helloFile = open('c:\\A\\wordpress.txt')
# read a file
helloContent = helloFile.read()
print(helloContent)
# return a list of strings from a file
aFile = open('c:\\A\\readlines.txt')
print('readlines is :', aFile.readlines())
# create a file and write sth to it
baconFile = open('c:\\A\\bacon.txt', 'w')
baconFile.write('hello bacon!\n')
baconFile.close()
baconFile = open('c:\\A\\bacon.txt', 'a')
baconFile.write('bacon is not a vegetable.')
baconFile.close()
baconFile = open('c:\\A\\bacon.txt')
content = baconFile.read()
print('read is :', content)
