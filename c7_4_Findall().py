import re
# without groups
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneNumRegex.findall('home : 489-555-6936, work : 546-889-8877'))

# with groups
phoneNumRegex1 = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
print(phoneNumRegex1.findall('home : 489-555-6936, work : 546-889-8877'))

# disconnect test
