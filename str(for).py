s=input("enter a string")
n=len(s)
if n<3:
    print("str")
res=" "
for i in range (n-3,n):
    res=res+s[i]
print(res)