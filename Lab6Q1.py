a=5 #for printing row entries
while a>-1: 
    b=5 #for printing column entries
    while b>-1: 
        print("(",a,",",b,") ",end="") #this function will print the pattern
        b-=1 #to avoid infinite loop
    a-=1 #to avoid infinite rows
    print()
