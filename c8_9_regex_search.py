import re
import os
numRegex = re.compile(r'\d\d\d-\d\d\d\-\d\d\d\d')
path = 'c:\\A\\num'
files = os.listdir(path)
print(files)
for file in files:
    f = open(path+os.sep+file)
    line = f.readlines()
    # print(line)
    for items in line:
        if items != '\n':
            Number = numRegex.findall(items)
            print(numRegex.findall(items))




