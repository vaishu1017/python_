n=int(input("enter n value"))
c=2
r=1
while c<=n%2 & r!=0:
    r=n%2
    c=c+1
if r<0:
    print("prime")
else:
    print("not prime")