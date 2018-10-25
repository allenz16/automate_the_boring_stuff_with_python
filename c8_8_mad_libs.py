bFile = open('c:\\A\\bFile.txt', 'r+')

while True:
    line = bFile.readline()
    if len(line) == 0:
        break
    if 'a' in line:
        sub = input('Type sth to replace \'a\' : ')
        line = line.replace('a', sub)
        bFile.writelines(line)
    if 'b' in line:
        sub = input('Type sth to replace \'b\' : ')
        line = line.replace('b', sub)
        bFile.writelines(line)
    if 'c' in line:
        sub = input('Type sth to replace \'c\' : ')
        line = line.replace('c', sub)
        bFile.writelines(line)
bFile.close()
bFile = open('c:\\A\\bFile.txt')
print(bFile.readlines())








