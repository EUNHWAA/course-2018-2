strInput ="aabbcccccca"
strOutput ="a2b2c6a1"

curChar=""
count=1
result=""

for i in strInput:
    if curChar==i:
        count= count +1
    else:
        if count !=0:
            count=1
    curChar=i
    print(curChar, count)