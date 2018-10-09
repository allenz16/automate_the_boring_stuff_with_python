import re
# call search()
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print('mo1 :', mo1.group())
mo2 = batRegex.search('The Adventures of Batwoman')
print('mo2 :', mo2.group())

# call findall()
batRegex1 = re.compile(r'Bat(wo)?men')
mo3 = batRegex1.findall('Batman and Batwomen')
print('mo3 :', mo3)

# search for phone number with or without the area code
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo4 = phoneRegex.search('485-520-5566 and 520-6699')
print('mo4 :', mo4.group())
mo5 = phoneRegex.findall('485-520-5566 and 520-6699')
print('mo5 :', mo5)

# matching zero or more with "*"
batRegex2 = re.compile(r'Bat(wo)*man')
mo6 = batRegex2.search('Batman')
print('mo6 :', mo6.group())
mo7 = batRegex2.search('Batwoman')
print('mo7 :', mo7.group())
mo8 = batRegex2.search('Batwowowowoman')
print('mo8 :', mo8.group())

# matching one or more with the "+"
batRegex3 = re.compile(r'Bat(wo)+man')
mo9 = batRegex3.search('Batwoman')
print('mo9 :', mo9.group())
mo10 = batRegex3.search('Batwowowowoman')
print('mo10 :', mo10.group())
mo11 = batRegex3.search('Batman')
print('mo11 :', mo11 == None)

# matching specific repetitions with curly brackets
haRegex = re.compile(r'(Ha){3}')
mo12 = haRegex.search('HaHaHa')
print('mo12 :', mo12.group())
mo13 = haRegex.search('Ha')
print('mo13 :', mo13 == None)

# greedy and non-greedy matching
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo14 = greedyHaRegex.search('HaHaHaHaHa')
print('mo14 :', mo14.group())
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo15 = nongreedyHaRegex.search('HaHaHaHaHa')
print('mo15 :', mo15.group())


