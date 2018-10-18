import pprint
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
# transfer 'cat' to string
print(pprint.pformat(cats))
# write the string to a file
fileObj = open('mycats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()

# import from mycats.py
import mycats
print(mycats.cats)
print(mycats.cats[0])
print(mycats.cats[0]['name'])
