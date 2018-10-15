import re
testRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = testRegex.findall('445-558-2693 and 456-556-5255')
print(mo)

# matching 1,230 3 numbers with a comma
reGex = re.compile(r'^\d{1,3}(,\d{3})*$')
mo1 = reGex.search('4')
print(mo1.group())

# matching last name as Nakamoto
nameRegex = re.compile(r'[a-z]\sNakamoto$')
mo2 = nameRegex.search(' Nakamoto')
print(mo2.group())
