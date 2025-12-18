n=int(input("Enter n value:"))
original=n
length=len(str(n))
result=0
while(n>0):
    digit=n%10
    result=result+digit**length
    n=n//10
if original==result:
    print("ArmStrong Number")
else:
    print("Not a ArmStrong Number")