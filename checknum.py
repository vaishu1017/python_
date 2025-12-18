n=int(input("enter n a valu"))
on=int(input("enter orginal value"))
res=0
while n>0:
    digit=n%10
    res=res+digit
    n=n//10
if on%res==0:
    print("hasard")
else:
    print("not hashard")