text = input("Enter a string: ")
word = {}  # use a dictionary to store character counts

for char in text:
    if char in word:
        word[char] += 1
    else:
        word[char] = 1

print("Character frequency:")
for char, count in word.items():
    print(f"{char}: {count}")
