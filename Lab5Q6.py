n=int(input("enter natural number:"))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" \t",end="")
    for j in range(1,i+1):
         print(j,"\t",end="")
    print()
