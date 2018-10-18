# Use shelve module to store data
import shelve
shelfFile = shelve.open('c:\\A\\mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()
# retrieve data in shelve
shelfFile = shelve.open('c:\\A\\mydata')
print(type(shelfFile))
print(shelfFile['cats'])
shelfFile.close()
# list data in shelve
shelfFile = shelve.open('c:\\A\\mydata')
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()

