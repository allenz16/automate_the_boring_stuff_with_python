# strong password detection
import re
# create password regex
passRegex = re.compile(r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}')
# capture a password and verify it
while True:
    password = input('please input your password : ')
    mo1 = passRegex.search(password)
    if mo1 is not None:
        print('nice password')
        break
    else:
        print('bad password')
print('done')







