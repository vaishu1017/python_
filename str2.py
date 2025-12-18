#str='ABCDEFGHIJK'
#print(str[0:3:])
str='ABCDEFGHIJK'
print(str[::2])


s=input("enter a string")
c=0
res=" "
for ch in s:
    if c<3:
        res=res+ch
        c=c+1
print(res)

