#str='ABCDEFGHIJK'
#print(str[::2])
s=input("enter sting")
c=0
res=''
while c<len(s):
    res=res+s[c]
    c=c+2
print(res)