s=input("enter string:")
words=s.split()
print(words)
first_largest=' '
second_largest=' '
for word in words:
    if(len(word)>len(first_largest)):
        second_largest=first_largest
        first_largest=word
    elif(len(word)>len(second_largest)and word!=first_largest):
            second_largest=word
print("First Biggest word:",first_largest)
if second_largest:
    print("second Biggest word:",second_largest)
else:
    print("Second longest word is not available")