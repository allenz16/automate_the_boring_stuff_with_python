import re
testRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = testRegex.findall('445-558-2693 and 456-556-5255')
print(mo)
