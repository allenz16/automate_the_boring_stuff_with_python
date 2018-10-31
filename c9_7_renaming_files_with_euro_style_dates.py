import shutil
import os
import re
datePattern = re.compile(r'''
    ^(.*?)           # all text before the date
    ((0|1)?\d)-      # one or two digits for the month     
    ((0|1|2|3)?\d)-  # one or two digits for the day
    ((19|20)\d\d)-   # four digits for the year
    (.*?)$           # all text after the date 
''', re.VERBOSE)
# Loop over the files in the working directory.
# print(os.listdir('c:\\A'))
for amerFilename in os.listdir('c:\\A'):
    print(amerFilename)
    mo = datePattern.search(amerFilename)
    if mo == None:
        continue
    # Get the different parts of the filename.
    print(mo)
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)
    # Form the European-style filename.
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
    # Get the full, absolute file paths
    absWorkingDir = os.path.abspath('c:\\A')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)
    # Rename the files.
    print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
    # shutil.move(amerFilename, euroFilename)




