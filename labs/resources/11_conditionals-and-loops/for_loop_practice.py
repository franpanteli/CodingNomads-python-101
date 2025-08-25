word = input("type some words: ")
i=0
result=""
for char in word:
    i=i+1
    if i%2==0:
        result += char.upper()
    else:
        result += char
print(result)