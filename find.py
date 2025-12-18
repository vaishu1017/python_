s=input("enter string")
ch=input("enter char")
pos=s.find(ch)
print(f"first ocuurance of{ch} is a index:",pos)

#
s=input("enter string")
ch=input("enter char to find")
pos=s.find(ch)
if pos==-1:
    print(f"char'{ch}'not found in str")
else:
    print(f"first ocuurance of{ch} is a index:",pos)