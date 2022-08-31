def marioPyramid(n):
    for i in range(1,n+1):
        print("*"*i)

def marioPyramid2(n):
    j=1
    for i in range(n+1,1,-1):   
        print(" "*i+"*"*j)
        j+=1
marioPyramid2(4)