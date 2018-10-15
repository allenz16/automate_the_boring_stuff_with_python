# strong password detection
import re
# capture a password
#password = input('please input your password : ')
# create password regex
passRule1 = re.compile(r'(?=.*?[A-Z])')
passRule2 = re.compile(r'at least 8 digit long')
passRule3 = re.compile(r'at least 1 num')
mo0 = passRule1.search('UkkKll26')
print(mo0.group())


