n=int(input("enter n value"))
i=1
print(f"factors of {n} are")
while i<=n:
    if n%i==0:
        print(i,end="")
    i=i+1

