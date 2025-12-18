s=input("enter a string ")
word=input("enter the word to search")
word=s.split()
found=False
for word in word:
    if word==word_to_search:
        found=True
        break
    if found:
        print(f" '(word_to_search)' is found is the string.")
    else:
        print(f" '(word_to_search)' is found is the string.")

        