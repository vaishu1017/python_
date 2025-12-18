def is_palindrom(word):
    length=len(word)
    for i in range(length//2):
        if word[i]!=word[length-1-i]:
            return False
        return True
s=input("enter a string")
word=s.split()
palindrom=[]
for word in word:
    if is_palindrom(word):
        palindrom.append(word)
if palindrom:
    print("found palindrom",palindrom)
else:
    print("found palindrom",palindrom)