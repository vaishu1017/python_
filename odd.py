def odd(s,e):
    while (s<=e):
        r=s%2
        if (r!=0):
            print(s,end=" ")
        s=s+1
s=int(input("enter start:"))
e=int(input("enter end:"))
odd(s,e)