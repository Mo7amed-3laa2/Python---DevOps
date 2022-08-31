lst = []

for i in range (0,5):
    lst.append(int(input(f"Enter the element no.{i+1}: ")))

lstAsce = lstDesc = lst

# Setting reverse = True/False sorts the list in the Descending/Ascending order.
lstAsce = sorted(lstAsce, reverse=False)
lstDesc = sorted(lstDesc, reverse=True)
 
print("list: ", lst)
print("list in Ascending: ", lstAsce)
print("list in Descending oreder: ", lstDesc)