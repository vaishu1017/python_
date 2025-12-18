i=int(input("enter start:"))
n=int(input("enter end:"))
sum=0
while i<=n:
    if i%2!=0:
        print(i)
        sum=sum+i
    i=i+1    
print("sum of odd",sum)

