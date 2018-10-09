import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo0 = phoneNumRegex.search('456-896-8899 and 789-568-8899')
mo1 = phoneNumRegex.findall('456-896-8899 and 789-568-8899')
print('mo0 :', mo0.group())
print('mo1 :', mo1)

phoneNumRegex1 = re.compile(r'\d{3}-\d{3}-\d{4}')
mo2 = phoneNumRegex1.search('456-896-8899 and 789-568-8899')
print('mo2 :', mo2.group())

phoneNumRegex2 = re.compile(r'(\d\d\d)-\d\d\d-\d\d\d\d')
mo3 = phoneNumRegex2.search('456-896-8899 and 789-568-8899')
mo4 = phoneNumRegex2.findall('456-896-8899 and 789-568-8899')
print('mo3 :', mo3.groups())
#areaCode, mainNumber = mo3.groups()
#print(areaCode)
#print(mainNumber)
print('mo4 :', mo4)

phoneNumRegex3 = re.compile(r'\(\d\d\d\)-\d\d\d-\d\d\d\d')
mo5 = phoneNumRegex3.findall('(456)-896-8899 and (789)-568-8899')
print('mo5 :', mo5)

heroRegex = re.compile(r'Batman|Tina Fey')
mo6 = heroRegex.search('Batman and Tina Fey')
mo7 = heroRegex.findall('Batman and Tina Fey')
print('mo6 :', mo6.group())
print('mo7 :', mo7)

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo8 = batRegex.findall('Batmobile and Batman and bat')
mo9 = batRegex.search('Batmobile and Batman and bat')
print('mo8 :', mo8)
print('mo9 :', mo9.group())


