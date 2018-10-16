import re
# def function
def strip_string(c, a=input('input sth : '), b=' '):

    regex = re.compile(b)
    mo = regex.sub(c, a)
    print(mo)


strip_string('-', b='_')








