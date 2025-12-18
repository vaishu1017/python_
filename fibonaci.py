n=int(input("enter n value"))
a=0
b=1
c=0

while a<=n:
    print(a)
    c=a+b
    a=b
    b=c
    cond=c+1
