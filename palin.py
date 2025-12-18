def is_palindrome(word):
    length = len(word)
    for i in range(length // 2):
        if word[i] != word[length - 1 - i]:
            return False
    return True

s = input("Enter a string: ")
word=s.split()

palindrome = []
non_palindrome= []

for word in word:
    if is_palindrome(word):
        palindrome.append(word)
    else:
        non_palindrome.append(word)

# Output
if palindrome:
    print("Palindrome found:", palindrome)
else:
    print("No palindrome  found.")

if non_palindrome:
    print("Non-palindrome is found:", non_palindrome)
else:
    print("No non-palindrome is found.")