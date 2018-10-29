import send2trash
baconFile = open('c:\\A\\bacon.txt', 'a')
baconFile.write('Bacon is not vegetable.')
baconFile.close()
send2trash.send2trash('c:\\A\\bacon.txt')
