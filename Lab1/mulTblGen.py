# Write a program that generate a multiplication table from 1 to the number passed.

# function to generate a table of some number.
def table (inputNum):
    lst = []
    for i in range(1,inputNum+1):
        lst.append(inputNum*i)
    return lst

inputNum = 5
tablesLst = []
lst = []

#loop to get all tables from 1 to the given number, by passing each number to the table function.
# then append each table to the tables list. 
for i in range(1,inputNum+1):
    tablesLst.append(table(i))

print(tablesLst)