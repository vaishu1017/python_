s=input("enter a string")
len=len(s)-1
i=0
found=True
while i<len:
    if s[i]!=s[len]:
        found=False
        break
    i=i+1
    len=len-1
if found:
    print("palindrom")
else:
    print("not palindrom")