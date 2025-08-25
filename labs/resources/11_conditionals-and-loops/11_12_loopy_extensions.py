# Proof that the following file is a .pdf file using a `for` loop.
# - Don't use the string method you've used to solve this before!
# - Don't use the `in` keyword to look for a sub-string!
# - Don't use any string slicing technique either!
#
# You'll see that it'll be tricky to solve this challenge with a loop :)
# Remember to use also other techniques you've learned,
# for example flags and conditional statements.

#ChatGPT solution
    #filename
filename = "document.pdf"
    #pdf extension
pdf_extension = ".pdf"
    #if this is True, then we have a pdf file
is_pdf = True  # flag to check

# First, check that the filename is at least as long as the extension
    #we know it's not a pdf if it's not long enough to have .pdf written at the end of it
if len(filename) < len(pdf_extension):
    is_pdf = False
else:
    # Compare each character from the end of the filename
    for i in range(1, len(pdf_extension)+1):
        #we are iterating through 'pdf' backwards, and through the filename backwards, to see if the two match
        #this is done through negative indexing
        if filename[-i] != pdf_extension[-i]:
            is_pdf = False
            #we stop if we find a match and change the valur of the is_pdf boolean
            break

#print out the result using an f string literal
if is_pdf:
    print(f"{filename} is a PDF file ✅")
else:
    print(f"{filename} is NOT a PDF file ❌")
