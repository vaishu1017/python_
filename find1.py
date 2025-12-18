

s = input("Enter a string: ")
word = input("Enter word to search: ")
index = 0
found = False

while index < len(s):
    index = s.find(word, index)
    if index == -1:
        break
    print(f"Found at index: {index}")
    found = True
    index += 1  # Move to next character to continue search

if not found:
    print("Not found")


