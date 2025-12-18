s=input("enter string:")
words=s.split()
sorted_words=sorted(words,key=len,reverse=True)
if(len(sorted_words)>=2):
    print("First Biggest word:",sorted_words[0])
    print("second Biggest word:",sorted_words[1])
if len(sorted_words)==1:
    print("Only one word present.First longest word:",sorted_words)
    print("second longest word not available")
else:
    print("NO words in the input")
