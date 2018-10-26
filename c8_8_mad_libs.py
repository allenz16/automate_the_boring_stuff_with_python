bFile = open('c:\\A\\bFile.txt', 'r')
cFile = open('c:\\A\\cFile.txt', 'w')
while True:
    line = bFile.readline()
    if len(line) == 0:
        break
    line = line.replace('a', 'A')
    line = line.replace('b', 'B')
    cFile.write(line)
cFile.close()
cFile = open('c:\\A\\cFile.txt')
print(cFile.readlines())










