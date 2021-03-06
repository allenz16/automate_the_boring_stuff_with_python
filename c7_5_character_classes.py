import re
xmasRegex = re.compile(r'\d+\s\w+')
mo = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print('mo :', mo)

# making your own character classes
vowelRegex = re.compile(r'[aeiouAEIOU]')
mo1 = vowelRegex.findall('Robocop eats baby food, BABY FOOD.')
print('mo1 :', mo1)

numRegex = re.compile(r'[0-5.]')
mo2 = numRegex.findall('1., 2., 3.')
print('mo2 :', mo2)

# negative character class
consonantRegex = re.compile(r'[^aeiouAEIOU]')
mo3 = consonantRegex.findall('Robot eats baby food. BABY FOOD.')
print('mo3 :', mo3)

# the caret ^ and dollar sign $ char
beginsWithHello = re.compile(r'^Hello')
mo4 = beginsWithHello.search('Hello World')
print('mo4 :', mo4.group())

endsWithNumber = re.compile(r'\d$')
mo5 = endsWithNumber.search('Your number is 42')
print('mo5 :', mo5.group())

wholeStingIsNum = re.compile(r'^\d+$')
print(wholeStingIsNum.search('54224215641231'))

# wildcard character
atRegex = re.compile(r'.at')
print(atRegex.findall('the cat in the hat sat on the flat mat'))

# matching everything with .*
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo6 = nameRegex.search('First Name: Al Last Name: Sweigart')
print('mo6 :', mo6.group(1))
print('mo6 :', mo6.group(2))

# greedy and non-greedy using .*
nongreedyRegex = re.compile(r'<.*?>')
mo7 = nongreedyRegex.search('<to serve man> for dinner.>')
print('mo7 :', mo7.group())
greedyRegex = re.compile(r'<.*>')
mo8 = greedyRegex.search('<to serve man> for dinner.>')
print('mo8 :', mo8.group())

# matching newlines with the dot character
noNewlineRegex = re.compile('.*')
print(noNewlineRegex.search('serve the public trust.\nprotect the innocent\nuphold the law').group())
newlineRegex = re.compile('.*', re.DOTALL)
print(newlineRegex.search('serve the public trust.\nprotect the innocent\nuphold the law').group())

# case-insensitive matching
robocop = re.compile(r'robocop', re.I)
print(robocop.search('Robocop is part man, part machine, all cop.').group())
print(robocop.search('ROBOCOP protects the innocent').group())

# substituting strings with the sub() method
nameRegex1 = re.compile(r'Agent \w+')
print(nameRegex1.sub('censored', 'Agent Alice gave the secret documents to Agent Bob.'))
agentNamesRegex = re.compile(r'Agent (\w)\w+')
print(agentNamesRegex.search('Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.').group())
print(agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))

# managing complex regex
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?
    (\s|-|\.)?
    \d{3}
    (\s|-|\.)?
    \d{4}
    (\s*(ext|x|ext.)\s*\d{2,5})?
)''', re.VERBOSE)

# combining re.IGNORECASE, re.DOTALL, re.VERBOSE
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)

