import re
datePattern = re.compile(r'''
    ^(.*)           # all text before the date
    ((0|1)?\d)-      # one or two digits for the month     
    ((0|1|2|3)?\d)-  # one or two digits for the day
    ((19|20)\d\d)   # four digits for the year
    (.*)$           # all text after the date 
''', re.VERBOSE)
mo = datePattern.search('11-26-2016')
print(mo.group())
