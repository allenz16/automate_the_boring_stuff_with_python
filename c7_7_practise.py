import re
# matching 1,230 3 numbers with a comma
reGex = re.compile(r'^\d{1,3}(,\d{3})*$')
mo1 = reGex.search('4')
print(mo1.group())

# matching a name with the last name as Nakamoto
nameRegex = re.compile(r'[A-Z][a-z]+\sNakamoto$')
mo2 = nameRegex.search('Haha Nakamoto')
print(mo2.group())

# matching a sentence where the first word is either Alice, Bob, or Carol; the second word is either eats, pets, or throws; the third word is apples, cats, or baseballs; and the sentence ends with a period? This regex should be case-insensitive.
randomRegex = re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.', re.I)
mo3 = randomRegex.search('Alice eats apples.')
print(mo3.group())

# test
testRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = testRegex.findall('445-558-2693 and 456-556-5255')
print(mo)

tRegex = re.compile(r'alice|bob|carol')
mo4 = tRegex.search('alice and bob')
print(mo4.group())


