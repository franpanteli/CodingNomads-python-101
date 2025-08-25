# Extract four words of edible food items from the sentence below.
# Use only string slicing to pick them out!
# Feel free to use pen and paper to number the indices
# and find the locations quicker.
#
# What dish can you make from these ingredients? :)

s = "They grappled with their leggins before going to see the buttercups flourish."
# for the index of the letters in the word variable
# a=0
# for i in s:
#     print(a,i)
#     a=a+1

#1 flour
flour = s[68:73]
print(flour)

#2 butter
butter = s[57:63]
print(butter)

#3 leg
leg = s[25:28]
print(leg)

#4 grape
grape =s[5:9]+s[21]
print(grape)

#battered grape flavoured chiken leg