# Write a program that prints the locations of "i" character in any string you added.

inputString = "Hello in iti, you are now part of iti community, cheer up iti student !"
indxLst = []  # list holding the index of all founded occurrences
indx = 0      # to follow every indx

for item in inputString:
    if item == "i":
        indxLst.append(indx)
    indx+=1

print(indxLst)
