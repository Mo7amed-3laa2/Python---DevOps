inputString = "Hello World !"
count = 0
'''
for item in inputString:
    if item in ["a", "e", "i", "o", "u"]:
        count+=1
print (f"Number of vowels in {inputString} is {count}")
'''
#---------------------------------------------------------
print(inputString.count(["a", "e", "i", "o", "u"]))


#---------------------------------------------------------
'''
if inputString in ["a", "e", "i", "o", "u"]:
        count+=1
print (f"Number of vowels in {inputString} is {count}")
'''