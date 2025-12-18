n=int(input("enter n value"))
i=1
sum=0
print(f"factors of {n} are")
while i<=n:
    if n%i==0:
        print(i,end="")
        sum=sum+i

    i=i+1
print("sum of factors",sum)
if sum==n:
    print("perfect")
else:
    print("imperfect")