import re
testRegex = re.compile(r'.*?')
mo = testRegex.findall('abc')
print('mo = ', mo)
