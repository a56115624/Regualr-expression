import re
phonenumbercheck = re.compile(r'\d\d-\d\d\d\d-\d\d\d\d')
mo = phonenumbercheck.search("call me at 02-8888-4894 by today")
print(mo.group())