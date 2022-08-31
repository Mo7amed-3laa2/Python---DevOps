# Write a program that remove all vowels from the input word and generate a brief version of it.
inputString = "Mohamed Alaa Eldeen Mostafa Abd Elhameed"
newString="" 

for item in inputString:
    if item not in ["a", "e", "i", "o", "u"]:
        newString=newString+item

print(newString)
