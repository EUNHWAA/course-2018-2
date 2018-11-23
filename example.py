import re

data="""
park 000-0000-0000
kim 111-1111-1111
lee 222-2222-2222
"""

pat=re.compile("(\d{3})[-](\d{4})[-]\d{4}")
print(pat.sub("\g<1>-\g<2>-####",data))